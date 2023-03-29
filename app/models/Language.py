from app import db

class Language(db.Model):

    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True)
    lang_code = db.Column(db.String, unique = True)

    def __init__(self, lang_code):
        self.lang_code = lang_code

    def __repr__(self):
        return self.lang_code