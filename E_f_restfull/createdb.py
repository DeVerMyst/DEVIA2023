from db import db, init_db  # Import the shared db instance
from app import app, User  # Import the app and User model

init_db(app)

# Use the app's context to perform operations
with app.app_context():
    # Drop all tables
    db.drop_all()

    # Create all tables
    db.create_all()

    # Add users
    user1 = User(username='john_doe', email='john@example.com')
    user2 = User(username='jane_doe', email='jane@example.com')
    user3 = User(username='bob_smith', email='bob@example.com')

    db.session.add_all([user1, user2, user3])
    db.session.commit()

print("Database created and populated.")
