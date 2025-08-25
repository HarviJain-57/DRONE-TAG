from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# ---------------------------
# Registration Table
# ---------------------------
class User(db.Model):
    __tablename__ = 'registration'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)  # Storing plain text password

    # Drone details (embedded into registration)
    tracker_id = db.Column(db.String(100), unique=True, nullable=False)
    uin = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    application = db.Column(db.String(150), nullable=False)

    registered_on = db.Column(db.DateTime, default=datetime.utcnow)


# ---------------------------
# Login History Table
# ---------------------------
class Login(db.Model):
    __tablename__ = 'login'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Also storing plain text password
    login_time = db.Column(db.DateTime, default=datetime.utcnow)


# ---------------------------
# Drone Location/Info Table
# ---------------------------
class DroneInfo(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    tracker_id = db.Column(db.String(100), unique=True, nullable=False)
    uin = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    application = db.Column(db.String(150), nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<DroneInfo {self.tracker_id}>"

# ---------------------------
# Drone data as it is fromserver
# ---------------------------

class DroneTagData(db.Model):
    __tablename__ = 'drone_tag_data'
    
    id = db.Column(db.Integer, primary_key=True)
    altitude = db.Column(db.Numeric)
    drone_application = db.Column(db.String(255))
    drone_category = db.Column(db.String(255))
    drone_uin_number = db.Column(db.String(100))
    latitude = db.Column(db.String(50))
    longitude = db.Column(db.String(50))
    maplink = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    tracker_id = db.Column(db.String(100))
