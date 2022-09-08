from flask_login import UserMixin
from datetime import datetime
from project.__init__ import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name_teacher = db.Column(db.String(1000))


class Marks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_student = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100))
    specialite = db.Column(db.String(100))

    note1 = db.Column(db.Float)
    note2 = db.Column(db.Float)
    note3 = db.Column(db.Float)
    note4 = db.Column(db.Float)
    note5 = db.Column(db.Float)
    note6 = db.Column(db.Float)
    note7 = db.Column(db.Float)
    note8 = db.Column(db.Float)
    note9 = db.Column(db.Float)
    note10 = db.Column(db.Float)
    note11 = db.Column(db.Float)
    note12 = db.Column(db.Float)
    note13 = db.Column(db.Float)
    note14 = db.Column(db.Float)
    note15 = db.Column(db.Float)

    notes = []
    coef_idl = [1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1]
    coef_rs = [2, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1]
    coef_se = [1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1]
    moyenne_generale_idl = db.Column(db.Float)
    moyenne_generale_rs = db.Column(db.Float)
    moyenne_generale_se = db.Column(db.Float)

    def calcul_moyenne_idl(self):
        self.moyenne_generale_idl = ((float(((float(self.note1) * float(self.coef_idl[0])) + (float(self.note2) * float(self.coef_idl[1])) + (
                        float(self.note3) * float(self.coef_idl[2]))))/3) + ( float(((float(self.note4) * float(self.coef_idl[3])) + (
                        float(self.note5) * float(self.coef_idl[4]))))/3) + (float(((float(self.note6) * float(self.coef_idl[5])) + (
                        float(self.note7) * float(self.coef_idl[6])) + (float(self.note8) * float(self.coef_idl[7]))))/4) + (float(((
                        float(self.note9) * float(self.coef_idl[8])) + (float(self.note10) * float(self.coef_idl[9])) + (
                        float(self.note11) * float(self.coef_idl[10]))))/5) + (float(((float(self.note12) * float(self.coef_idl[11])) + (
                        float(self.note13) * float(self.coef_idl[12])) + (float(self.note14) * float(self.coef_idl[13]))))/3)) / 5

    def calcul_moyenne_rs(self):
        self.moyenne_generale_rs = ((float(((float(self.note1) * float(self.coef_rs[0])) + (float(self.note2) * float(self.coef_rs[1])) + (
                        float(self.note3) * float(self.coef_rs[2]))))/5) + ( float(((float(self.note4) * float(self.coef_rs[3])) + (
                        float(self.note5) * float(self.coef_rs[4]))))/3) + (float(((float(self.note6) * float(self.coef_rs[5])) + (
                        float(self.note7) * float(self.coef_rs[6])) + (float(self.note8) * float(self.coef_rs[7]))))/4) + (float(((
                        float(self.note9) * float(self.coef_rs[8])) + (float(self.note10) * float(self.coef_rs[9])) + (
                        float(self.note11) * float(self.coef_rs[10]))))/4) + (float(((float(self.note12) * float(self.coef_rs[11])) + (
                        float(self.note13) * float(self.coef_rs[12])) + (float(self.note14) * float(self.coef_rs[13]))))/3)) / 5

    def calcul_moyenne_se(self):
        self.moyenne_generale_se = ((float(((float(self.note1) * float(self.coef_se[0])) + (float(self.note2) * float(self.coef_se[1])) + (
                        float(self.note3) * float(self.coef_se[2]))))/4) + ( float(((float(self.note4) * float(self.coef_se[3])) + (
                        float(self.note5) * float(self.coef_se[4]))))/4) + (float(((float(self.note6) * float(self.coef_se[5])) + (
                        float(self.note7) * float(self.coef_se[6])) + (float(self.note8) * float(self.coef_se[7]))))/4) + (float(((
                        float(self.note9) * float(self.coef_se[8])) + (float(self.note10) * float(self.coef_se[9])) + (
                        float(self.note11) * float(self.coef_se[10]))))/4) + (float(((float(self.note12) * float(self.coef_se[11])) + (
                        float(self.note13) * float(self.coef_se[12])) + (float(self.note14) * float(self.coef_se[13]))))/3)) / 5

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
