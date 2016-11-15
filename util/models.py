from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    time = db.Column(db.Integer, unique=False)

    def __init__(self, username=None, time=None):
        self.username = username
        self.time = time

    def __repr__(self):
        return '<User %r>' % (self.username)
