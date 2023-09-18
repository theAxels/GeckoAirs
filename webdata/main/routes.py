
from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user

# from webdata.__init__ import app
# sama aja dgn bawah
from webdata import bcrypt, db

from webdata.models import User, City, SeatType, Booking
import datetime

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
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
            
            # print(fromCityID, toCityID, departing, seattypeID);
            redirect(url_for('main.search_result'))
            
    seattypes = SeatType.query.all()
    cities = City.query.all()
    return render_template('index.html', cities=cities, seattypes=seattypes)

@main.route('/result', methods=['GET', 'POST'])
def search_result():
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
            
            # print(fromCityID, toCityID, departing, seattypeID);
            redirect(url_for('main.search_result'))
            
    seattypes = SeatType.query.all()
    cities = City.query.all()
    # return render_template('index.html', cities=cities, seattypes=seattypes)
        
    current_time = datetime.datetime.utcnow()
    print(current_time)
    return render_template('search_result.html', cities=cities, seattypes=seattypes, current_time=current_time)    

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

'''
lagi di halaman html 
url_for('main.pay', booking_id=booking.booking_id)
'''