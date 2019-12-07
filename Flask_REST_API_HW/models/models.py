from db import db


class TenantsModel(db.Model):
    name = db.Column(db.String)
    PassportID = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Sex = db.Column(db.String)
    Address = db.Column(db.String)
    RoomNumber = db.Column(db.Integer)


class RoomsModel(db.Model):
    Number = db.Column(db.Integer)
    Level = db.Column(db.Integer)
    Status = db.Column(db.String)
    Price = db.Column(db.Integer)


class StaffModel(db.Model):
    name = db.Column(db.String)
    PassportID = db.Column(db.Integer)
    Position = db.Column(db.String)
    Salary = db.Column(db.Integer)
