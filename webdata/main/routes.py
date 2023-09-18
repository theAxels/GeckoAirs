
from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import text
from flask_login import login_required, login_user, logout_user


from webdata import bcrypt, db
from webdata.models import User, City, City, SeatType, Flight, Route, Airlines, datetime, Booking
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
            user = User(dob = dob,name = name, phone_number = phone_number, gender = gender, email = email, password = hashed)
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
                redirect(url_for('main.result'))
            
            hashed = bcrypt.generate_password_hash(password).decode('UTF-8')
            user = User(dob = dob,name = name, phone_number = phone_number, gender = gender, email = email, password = hashed)
            db.session.add(user)
            db.session.commit()
            flash('Accounts created successfully! please login ', 'success')
            redirect(url_for('main.result'))
        if action == 'search':
            fromCityID = request.form.get('fromCity') 
            toCityID = request.form.get('toCity')
            departing = request.form.get('departing')
            seattypeID = request.form.get('seattype')
            
            return redirect(url_for('main.result', fromCityID=fromCityID, toCityID=toCityID, departing=departing, seattypeID=seattypeID))
        
        if action == 'book':
            if not current_user.is_authenticated:
                flash('Need login to book flight !', 'warning')
            userId = current_user.user_id
            flightId = request.form.get('flight_id')
            booking_status = 'unpaid'
            seattypeID = request.form.get('seat_type_id')
            payment_amount = request.form.get('payment_amount')
            booking_date = datetime.datetime.now()
            
            book = Booking(user_id=userId, flight_id=flightId, booking_status = booking_status, seat_type_id = seattypeID, payment_amount = payment_amount, booking_date=booking_date)

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
        SELECT f.flight_id, a.airline_name, c1.city_name, DATE_FORMAT(TIME(f.flight_date), '%H:%i') AS 'Departure Time', CONCAT(FLOOR(r.duration_hours/60), 'h ', (r.duration_hours%60), 'm') AS 'Duration', c2.city_name, DATE_FORMAT(DATE_ADD(TIME(f.flight_date), INTERVAL r.duration_hours MINUTE), '%H:%i') AS 'Arrival Time', f.flight_price + (f.flight_price * st.seat_type_price / 100) AS 'price'
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
        total = result[7]
        formatted_price = str(locale.format_string("%.0f", total, grouping=True))
        formatted_price = formatted_price.replace(',', '.')
        flight = {
            'flight_id': result[0],
            'airline_name': result[1],
            'Departure City': result[2],
            'Departure Time': result[3],
            'Duration': result[4],
            'Destination City': result[5],
            'Arrival Time': result[6],
            'payment_amount' : result[7],
            'price' : formatted_price,
            'seat_type_id' : seattypeID
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
    
@main.route('/pay/<int:booking_id>')
@login_required
def pay(booking_id):
    booking = Booking.query.get(booking_id)
    
    if booking.user_id != current_user.user_id:
        flash("You don't have access to this page!", "danger")
        return redirect(url_for('main.index'))
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
                redirect(url_for('main.about'))
            
            hashed = bcrypt.generate_password_hash(password).decode('UTF-8')
            user = User(dob = dob,name = name, phone_number = phone_number, gender = gender, email = email, password = hashed)
            db.session.add(user)
            db.session.commit()
            flash('Accounts created successfully! please login ', 'success')
            redirect(url_for('main.about'))
    return render_template('about.html')

'''
lagi di halaman html 
url_for('main.pay', booking_id=booking.booking_id)
'''