from app import db


class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=False, nullable=False)
    license = db.Column(db.String(20), unique=True, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime, nullable=False)
    contact = db.Column(db.String(15), nullable=False)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username


class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    license_num = db.Column(db.String(20), unique=True, nullable=False)
    model = db.Column(db.String(40), nullable=False)
    brand = db.Column(db.String(40))
    color = db.Column(db.String(40))

    def __init__(self, message, sender):
        self.message = message
        self.sender = sender

    def __repr__(self):
        return '<Message %r>' % self.message