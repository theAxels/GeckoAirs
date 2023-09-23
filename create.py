from flask import Flask
from webdata.models import *
from flask_sqlalchemy import SQLAlchemy
from webdata.config import Config

from webdata import app, db, bcrypt

# def main():
#     Flight1 = Flight(flight_number = "GA003" , RouteID = 11, flight_price = 1_200_000, AirlineID = 1, SeatTypeID = 1, Seat = 40)
#     Flight2 = Flight(flight_number = "GA003" , RouteID = 11, flight_price = 1_985_000, AirlineID = 1, SeatTypeID = 2, Seat = 10)
#     Flight3 = Flight(flight_number = "GA003" , RouteID = 11, flight_price = 2_950_000, AirlineID = 1, SeatTypeID = 3, Seat =6)
#     db.session.add(Flight1)
#     db.session.add(Flight2)
#     db.session.add(Flight3)
#     db.session.commit()
    
    
# def main():
#     payment1 = Payment(booking_id = 6 , payment_date = "2022-10-04" , paymentmethod= "BCA")
#     payment2 = Payment(booking_id = 8 , payment_date = "2023-04-10" , paymentmethod = "BNI")
#     payment3 = Payment(booking_id = 7 , payment_date = "2023-04-10" , paymentmethod = "BNI")
#     payment4 = Payment(booking_id = 9 , payment_date = "2023-04-10" , paymentmethod = "ShopeePay")
    
#     db.session.add(payment1)
#     db.session.add(payment2)
#     db.session.add(payment3)
#     db.session.add(payment4)
#     db.session.commit()
    
def main():
    refund1 = RefundPayment(payment_id = 37 , refund_date = "2022-10-04")
    refund2 = RefundPayment(payment_id = 38 , refund_date = "2023-04-10")
    refund3 = RefundPayment(payment_id = 39 , refund_date = "2023-04-10")
    
    db.session.add(refund1)
    db.session.add(refund2)
    db.session.add(refund3)
    db.session.commit()

# def main():
#     Airline1 = Airlines()
    

if __name__ == '__main__':
    with app.app_context():
        main()  

'''
INSERT INTO `users` (`date_of_birth`, `name`, `phone_number`, `email`, `gender`, `password`) VALUES
('2004-11-28', 'Jeff', '0811765971', 'ppti.jeffersontimotius@gmail.c', 'Male', '$2b$12$HyfPeYoXfbob6sbbdcBPIuGLetee5t/l82kXcnqhcbwdqmtcA1Jpa'),
('2000-05-15', 'Alice', '0812345678', 'alice@example.com', 'Female', '$2b$12$ehQn13MkhanmSLydSo2szeWixV4ttmHsVQcJ5L/HL9MBwZc1LMWKy'),
('1995-09-03', 'Michael', '0809876543', 'michael@example.com', 'Male', '$2b$12$Vh7tv/mSw4dZh/o4X00dqOGg9dPhpUwOqv8MJc8GIaCIKyagMXEUC'),
('2001-07-22', 'Emily', '0854321098', 'emily@example.com', 'Female', '$2b$12$BvgRGGfIHu5mFb8QD5rM.eIsJILRlQj.oG2zpXxjrUzxvJzA9ImQy'),
('1998-12-10', 'Daniel', '0810112233', 'daniel@example.com', 'Male', '$2b$12$iWAKALXapLYSnYr/OHefGedJVU96zj1LawONQj6ErymKhUIY46t8y'),
('1993-04-17', 'Olivia', '0823456789', 'olivia@example.com', 'Female', '$2b$12$nnjcbSY8/.EO4gI/X6C4IO1RIBbtimPpc8rFmumk.NhzPCEwABlRS'),
('1993-04-17', 'Olivia', '0823456789', 'olivia1@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('2002-08-12', 'William', '0811223344', 'william@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1990-03-25', 'Sophia', '0876543210', 'sophia@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('2003-01-08', 'James', '0856789012', 'james@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1997-06-19', 'Ava', '0812345678', 'ava@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1994-10-30', 'Benjamin', '0833333333', 'benjamin@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('2005-02-14', 'Mia', '0898765432', 'mia@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1988-07-07', 'Liam', '0808080808', 'liam@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('2000-12-02', 'Ella', '0865432109', 'ella@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1996-09-14', 'Ethan', '0878787878', 'ethan@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1991-05-07', 'Charlotte', '0819191919', 'charlotte@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('2004-03-01', 'Henry', '0858585858', 'henry@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1999-11-11', 'Amelia', '0842424242', 'amelia@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1992-08-23', 'Noah', '0824242424', 'noah@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('2002-06-06', 'Sofia', '0836363636', 'sofia@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1989-12-12', 'Emma', '0875757575', 'emma@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('2003-09-09', 'Alexander', '0898989898', 'alexander@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1998-04-04', 'Mason', '0811111111', 'mason@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('1995-02-02', 'Lily', '0859595959', 'lily@example.com', 'Female', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC'),
('2001-07-07', 'Daniel', '0849494949', 'daniel10@example.com', 'Male', '$2b$12$NvYOzuga0i2qxowNTo8kJuOoFlvucGExpeRRkmbDe2yTlle6.xTSC');

'''
