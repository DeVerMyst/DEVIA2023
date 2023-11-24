# manager.py
from model import User, session

def create_user(username, email):
    new_user = User(username=username, email=email)
    session.add(new_user)
    session.commit()

def get_all_users():
    return session.query(User).all()
