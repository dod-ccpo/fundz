from fundz.app import db

class TaskOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String)
