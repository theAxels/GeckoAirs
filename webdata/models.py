from webdata import db, loginManager
from flask_login import UserMixin
import datetime
@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class City(db.Model):
    __tablename__ = 'cities'
    city_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(60), nullable=False)
    city_code = db.Column(db.String(5), nullable=False)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    name = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    gender = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'{self.user_id} - {self.name} - {self.email}'
    
    def get_id(self):
        return str(self.user_id)
    
    def calculate_age(self):
        return datetime.datetime.now().year - self.date_of_birth.year
    
class Airlines(db.Model):
    __tablename__ = 'airlines'
    airline_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    airline_name = db.Column(db.String(25), nullable=False)
    
class Flight(db.Model):
    __tablename__ = 'flights'
    flight_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_number = db.Column(db.String(20), nullable=False)
    flight_date = db.Column(db.Date, default=datetime.date.today)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.route_id'), nullable=False)
    flight_price = db.Column(db.Integer, nullable=False)
    airline_id = db.Column(db.Integer, db.ForeignKey('airlines.airline_id'), nullable=False)
    seat_type_id = db.Column(db.Integer, db.ForeignKey('seat_types.seat_type_id'), nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    
    
class SeatType(db.Model):
    __tablename__ = 'seat_types'
    seat_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seat_type_name = db.Column(db.String(25), nullable=False)
    seat_type_price = db.Column(db.Integer, nullable=False)
    
class Booking(db.Model):
    __tablename__ = 'bookings'
    booking_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.flight_id'), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False)
    booking_status = db.Column(db.String(20), nullable=False)
    seat_type_id = db.Column(db.Integer, db.ForeignKey('seat_types.seat_type_id'), nullable=False)
    payment_amount = db.Column(db.Integer, nullable=False)
    
class Payment(db.Model):
    __tablename__ = 'payments'
    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('bookings.booking_id'), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    
class Route(db.Model):
    __tablename__ = 'routes'
    route_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origin_city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'), nullable=False)
    destination_city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'), nullable=False)
    duration_hours = db.Column(db.Integer, nullable=False)