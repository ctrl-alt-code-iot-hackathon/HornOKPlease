from app import db
from app.models import Driver, Vehicles


def insert_details(username, license, gender, dob, contact):
    print('inserting')
    new_driver = Driver(username = username, license = license, gender = gender, dob = dob, contact = contact)
    db.session.add(new_driver)
    db.session.commit()
    print('inserted')


# def verify_username(username):
#     user = User.query.filter_by(username=username).first()
#     if not user:
#         new_user = User(username=username)
#         db.session.add(new_user)
#         db.session.commit()


# def get_all_messages():
#     return Message.query.all()


# def add_message(message, username):
#     sender_id = User.query.filter_by(username=username).first().id
#     new_msg = Message(message=message, sender=sender_id)
#     db.session.add(new_msg)
#     db.session.commit()