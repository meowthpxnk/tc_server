from app import db

class CategoryTranslate(db.Model):

    __tablename__ = 'category_translates'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship('Category', backref=db.backref('translates', lazy='dynamic'))
    
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    language = db.relationship('Language', backref=db.backref('categories', lazy='dynamic'))

    def __init__(self, name, category_id, language_id):
        self.name = name

        self.category_id = category_id
        self.language_id = language_id

    def getInfo(self):
        
        return {
            "name": self.name
        }