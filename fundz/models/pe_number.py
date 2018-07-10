from fundz.database import db

class PENumber(db.Model):
    number = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)

    def __repr__(self):
        return "<PENumber(number='{}', description='{}')>".format(
            self.number, self.description)
