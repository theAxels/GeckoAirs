
from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from flask_login import login_required, login_user, logout_user


from webdata import bcrypt, db
from webdata.models import User, City, City, SeatType, Flight, Route, Airlines, datetime, Booking, RefundPayment, Payment
import datetime
import locale

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        action = request.args.get('action')
        print(action)
        if action == 'login':
            email = request.form.get('email1')
            # print(email)
            user = User.query.filter_by(email=email).first()
            # print(user)
            if user :
                password = request.form.get('password1')
                check = bcrypt.check_password_hash(user.password, password)
                
                if check == True:
                    login_user(user)
                    flash("User has been logged in succesfully!", 'success')
                    return redirect(url_for('main.index'))
                flash("Login Failed. Incorrect  password!", 'danger')
                return redirect(url_for('main.index'))
            flash("Login Failed. Unfound  email!", 'danger')
            return redirect(url_for('main.index'))
        if action == 'register':
            dob = request.form.get('dob')
            name = request.form.get('name')
            phone_number = request.form.get('phone_number')
            gender = request.form.get('gender')
            email = request.form.get('email2')
            password = request.form.get('password2')
            
            check = User.query.filter_by(email = email).first()
            
            if check : 
                flash('Email for registration is not valid or already used', 'danger')
                redirect(url_for('main.index'))
            
            hashed = bcrypt.generate_password_hash(password).decode('UTF-8')
            user = User(date_of_birth = dob,name = name, phone_number = phone_number, gender = gender, email = email, password = hashed)
            db.session.add(user)
            db.session.commit()
            flash('Accounts created successfully! please login ', 'success')
            redirect(url_for('main.index'))
        if action == 'search':
            fromCityID = request.form.get('fromCity') 
            toCityID = request.form.get('toCity')
            departing = request.form.get('departing')
            seattypeID = request.form.get('seattype')
            print(fromCityID, toCityID, departing, seattypeID)
            return redirect(url_for('main.result', fromCityID=fromCityID, toCityID=toCityID, departing=departing, seattypeID=seattypeID))
            
    seattypes = SeatType.query.all()
    cities = City.query.all()
    return render_template('index.html', cities=cities, seattypes=seattypes)

@main.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        action = request.args.get('action')
        if action == 'login':
            email = request.form.get('email1')
            # print(email)
            user = User.query.filter_by(email=email).first()
            # print(user)
            if user :
                password = request.form.get('password1')
                check = bcrypt.check_password_hash(user.password, password)
                
                if check == True:
                    login_user(user)
                    flash("User has been logged in succesfully!", 'success')
                    return redirect(url_for('main.result'))
                flash("Login Failed. Incorrect  password!", 'danger')
                return redirect(url_for('main.result'))
            flash("Login Failed. Unfound  email!", 'danger')
            return redirect(url_for('main.result'))
        if action == 'register':
            dob = request.form.get('dob')
            name = request.form.get('name')
            phone_number = request.form.get('phone_number')
            gender = request.form.get('gender')
            email = request.form.get('email2')
            password = request.form.get('password2')
            
            check = User.query.filter_by(email = email).first()
            
            if check : 
                flash('Email for registration is not valid or already used', 'danger')
                return redirect(url_for('main.result'))
            
            hashed = bcrypt.generate_password_hash(password).decode('UTF-8')
            user = User(date_of_birth = dob,name = name, phone_number = phone_number, gender = gender, email = email, password = hashed)
            db.session.add(user)
            db.session.commit()
            flash('Accounts created successfully! please login ', 'success')
            return redirect(url_for('main.result'))
        if action == 'search':
            fromCityID = request.form.get('fromCity') 
            toCityID = request.form.get('toCity')
            departing = request.form.get('departing')
            seattypeID = request.form.get('seattype')
            
            return redirect(url_for('main.result', fromCityID=fromCityID, toCityID=toCityID, departing=departing, seattypeID=seattypeID))
        
        if action == 'book':
            if not current_user.is_authenticated:
                flash('Need login to book flight !', 'danger')
                return redirect(url_for('main.result'))
            userId = current_user.user_id
            flightId = request.form.get('flight_id')
            booking_status = 'Unpaid'
            booking_date = datetime.datetime.now()
            
            book = Booking(user_id=userId, flight_id=flightId, booking_status = booking_status, booking_date=booking_date)

            db.session.add(book)
            db.session.commit()

            # Redirect to the payment page with the newly created booking_id
            flash('Booking successful! Proceed to payment.', 'success')
            return redirect(url_for('main.pay', booking_id=book.booking_id))
            
    fromCityID = request.args.get('fromCityID')
    toCityID = request.args.get('toCityID')
    departing = request.args.get('departing')
    seattypeID = request.args.get('seattypeID')

    
    seattypes = SeatType.query.all()
    cities = City.query.all()
    # return render_template('index.html', cities=cities, seattypes=seattypes)
    
    query = text('''
        SELECT f.flight_id, a.airline_name, c1.city_name, c1.city_code, DATE_FORMAT(TIME(f.flight_date), '%H:%i') AS 'Departure Time', CONCAT(FLOOR(r.duration_hours/60), 'h ', (r.duration_hours%60), 'm') AS 'Duration', c2.city_name, c2.city_code, DATE_FORMAT(DATE_ADD(TIME(f.flight_date), INTERVAL r.duration_hours MINUTE), '%H:%i') AS 'Arrival Time', f.flight_price + (f.flight_price * st.seat_type_price / 100) AS 'price', f.available_seats
        FROM flights f
        JOIN routes r ON r.route_id = f.route_id
        JOIN airlines a ON a.airline_id = f.airline_id
        JOIN cities c1 ON c1.city_id = r.origin_city_id
        JOIN cities c2 ON c2.city_id = r.destination_city_id
        JOIN seat_types st ON st.seat_type_id = f.seat_type_id
        WHERE c1.city_id = :from_city_id AND c2.city_id = :to_city_id AND st.seat_type_id = :seat_type_id AND DATE(f.flight_date) >= :departing;
    ''')
    
    # Bind query parameters
    params = {
        'from_city_id': fromCityID,
        'to_city_id': toCityID,
        'seat_type_id': seattypeID,
        'departing': departing
    }

    # Execute the query and fetch the results
    results = db.session.execute(query, params)
    # flights = [result for result in results]
    flights = []
    for result in results:
        total = result[9]
        formatted_price = str(locale.format_string("%.0f", total, grouping=True))
        formatted_price = formatted_price.replace(',', '.')
        flight = {
            'flight_id': result[0],
            'airline_name': result[1],
            'Departure City': result[2],
            'Departure Code': result[3],
            'Departure Time': result[4],
            'Duration': result[5],
            'Destination City': result[6],
            'Destination Code': result[7],
            'Arrival Time': result[8],
            'payment_amount' : result[9],
            'price' : formatted_price,
            'seat_type_id' : seattypeID,
            'available_seats' : result[10]
        }
        flights.append(flight)
    print(flights)
    return render_template('search_result.html', cities=cities, seattypes=seattypes, flights=flights)    

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("User has been logged out succesfully!", "success")
    return redirect(url_for('main.index'))

# @app.route('/add_dummy_data')
# def add_dummy_data():
#     temp = 'admin123'
    
#     hashed = bcrypt.generate_password_hash(temp).decode('UTF-8')
    # check = bcrypt.check_password_hash(hashed, 'admin123')
    # return str(check) +' '+ str(hashed)
    # for i in range(5):
    #     from random import randint
    #     ge = ['Female', 'Male']
    #     sl = ge[randint(0,1)]
    #     user = User(dob='2022-05-13', name=f'user{i}', phone_number='081234567890', email=f"user{i}@gmail.com", age=randint(1, 100), gender=sl, password=hashed)
    #     db.session.add(user)
    #     db.session.commit()
    # return 'ok'
    
@main.route('/pay/<int:booking_id>', methods=['GET', 'POST'])
@login_required
def pay(booking_id):
    booking = Booking.query.get(booking_id)
    
    if not booking:
        flash("Booking not found!", "danger")
        return redirect(url_for('main.index'))
    
    if booking.user_id != current_user.user_id:
        flash("You don't have access to this page!", "danger")
        return redirect(url_for('main.index'))
    
    if booking.booking_status == 'Paid':
        flash("You have already paid for this booking!", "danger")
        return redirect(url_for('main.manage'))
    
    if request.method == 'POST':
        booking.booking_status = 'Paid'
        payment_method = request.form.get('PaymentSelect')
        payment_date = datetime.datetime.now()
        
        payment = Payment(booking_id=booking_id, payment_date=payment_date, paymentmethod=payment_method , payment_status = "Paid")
        db.session.add(payment)
        db.session.commit()
        return redirect(url_for('main.thankyou', booking_id=booking.booking_id))
    
    
    
    current_time = datetime.datetime.utcnow()
    print(current_time)
    return render_template('payment.html', booking=booking, current_time=current_time)


@main.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        action = request.args.get('action')
        if action == 'login':
            email = request.form.get('email1')
            # print(email)
            user = User.query.filter_by(email=email).first()
            # print(user)
            if user :
                password = request.form.get('password1')
                check = bcrypt.check_password_hash(user.password, password)
                
                if check == True:
                    login_user(user)
                    flash("User has been logged in succesfully!", 'success')
                    return redirect(url_for('main.result'))
                flash("Login Failed. Incorrect  password!", 'danger')
                return redirect(url_for('main.result'))
            flash("Login Failed. Unfound  email!", 'danger')
            return redirect(url_for('main.about'))
        if action == 'register':
            dob = request.form.get('dob')
            name = request.form.get('name')
            phone_number = request.form.get('phone_number')
            gender = request.form.get('gender')
            email = request.form.get('email2')
            password = request.form.get('password2')
            
            check = User.query.filter_by(email = email).first()
            
            if check : 
                flash('Email for registration is not valid or already used', 'danger')
                return redirect(url_for('main.about'))
            
            hashed = bcrypt.generate_password_hash(password).decode('UTF-8')
            user = User(date_of_birth = dob,name = name, phone_number = phone_number, gender = gender, email = email, password = hashed)
            db.session.add(user)
            db.session.commit()
            flash('Accounts created successfully! please login ', 'success')
            return redirect(url_for('main.about'))
    return render_template('about.html')



@main.route('/manage_bookings',  methods=['GET', 'POST'])
def manage():
    if not current_user.is_authenticated:
        flash('Need login to manage book !', 'danger')
        return redirect(url_for('main.index'))
    userId = current_user.user_id
    query = text('''
       SELECT b.booking_id, f.flight_number, a.airline_name, c1.city_name,  DATE_FORMAT(TIME(f.flight_date), '%H:%i') AS 'Departure Time', CONCAT(FLOOR(r.duration_hours/60), 'h ', (r.duration_hours%60), 'm') AS 'Duration', c2.city_name, DATE_FORMAT(DATE_ADD(TIME(f.flight_date), INTERVAL r.duration_hours MINUTE), '%H:%i') AS 'Arrival Time', f.flight_price + (f.flight_price * st.seat_type_price / 100) AS 'price', b.booking_status
        FROM bookings b
        JOIN flights f ON f.flight_id=b.flight_id
        JOIN airlines a ON a.airline_id=f.airline_id
        JOIN seat_types st ON st.seat_type_id=f.airline_id
        JOIN routes r ON r.route_id=f.route_id
        JOIN cities c1 ON c1.city_id=r.origin_city_id
        JOIN cities c2 ON c2.city_id=r.destination_city_id
        WHERE b.user_id = :user_Id;
    ''')
    
    params = {
        'user_Id': userId,
    }
    results = db.session.execute(query, params)
    books = []
    for result in results:
        total = result[8]
        formatted_price = str(locale.format_string("%.0f", total, grouping=True))
        formatted_price = formatted_price.replace(',', '.')
        book = {
            'booking_id' : result[0],
            'flight_number': result[1],
            'airline_name': result[2],
            'Departure City': result[3],
            'Departure Time': result[4],
            'Duration': result[5],
            'Destination City': result[6],
            'Arrival Time': result[7],
            'price' : formatted_price,
            'booking_status' : result[9]
        }
        books.append(book)
    print(books)
    
    if request.method == 'POST':
        action = request.args.get('action')
        if action == 'pay':
            booking_id = request.form.get('booking_id')
            print(booking_id)
            return redirect(url_for('main.pay', booking_id=booking_id))
        
        elif action == 'refund':
            booking_id = request.form.get('booking_id')
            payment = db.session.query(Payment).filter_by(booking_id=booking_id).first()
            payment_id = payment.payment_id
            
            booking = db.session.query(Booking).filter_by(booking_id=booking_id).first()
            booking.booking_status = "Refund"
            db.session.commit()
            
            refund = RefundPayment(payment_id=payment_id, refund_date=datetime.datetime.now())
            db.session.add(refund)
            db.session.commit()
            
            flash('Bookings refund successfull!', 'success')
            return redirect(url_for('main.manage'))
    
    return render_template('manage_bookings.html', books = books)

@main.route('/thankyou/<int:booking_id>')
@login_required
def thankyou(booking_id):
    
    book = Booking.query.get(booking_id)
    if not book:
        flash("Booking not found!", "danger")
        return redirect(url_for('main.index'))
    
    prev = request.referrer
    prev = list(str(prev).split('/'))
    check = '/'+'/'.join(prev[-2:])
    
    if (check != url_for('main.pay', booking_id=booking_id)):
        flash('You are not allowed to access this page!', 'danger')
        return redirect(url_for('main.index'))
    
    return render_template('thankyou.html')

@main.route('/cancel_booking/<int:id>', methods=['GET', 'POST'])
def cancel_booking(id):
    if not current_user.is_authenticated:
        flash('Need login to cancel book !', 'danger')
        return redirect(url_for('main.index'))
    userId = current_user.user_id
    booking_id = id
    booking = Booking.query.get(booking_id)
    if not booking:
        flash("Booking not found!", "danger")
        return redirect(url_for('main.index'))
    
    if booking.user_id != current_user.user_id:
        flash("You don't have access to this page!", "danger")
        return redirect(url_for('main.index'))
    
    if booking.booking_status == 'Paid':
        flash("You have already paid for this booking!", "danger")
        return redirect(url_for('main.manage'))
    
    booking.booking_status = 'Cancelled'
    booking.cancel_date = datetime.datetime.now()
    db.session.commit()
    
    flash('Bookings cancelled successfull!', 'success')
    return redirect(url_for('main.manage'))
    
'''
lagi di halaman html 
url_for('main.pay', booking_id=booking.booking_id)
'''