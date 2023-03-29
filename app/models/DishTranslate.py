from app import db

class DishTranslate(db.Model):

    __tablename__ = 'dish_translates'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    portion = db.Column(db.String)
    ingredients = db.Column(db.String)
    description = db.Column(db.String)

    dish_id = db.Column(db.Integer, db.ForeignKey('dishes.id'))
    dish = db.relationship('Dish', backref=db.backref('translates', lazy='dynamic'))
    
    language_id = db.Column(db.Integer, db.ForeignKey('languages.id'))
    language = db.relationship('Language', backref=db.backref('dishes', lazy='dynamic'))

    def __init__(self, name, portion, ingredients, description, dish_id, language_id):
        self.name = name
        self.portion = portion
        self.ingredients = ingredients
        self.description = description
        
        self.dish_id = dish_id
        self.language_id = language_id

    def getInfo(self):
        
        return {
            "name": self.name,
            "portion": self.portion,
            "ingredients": self.ingredients,
            "description": self.description,
        }
    
    def getSemiInfo(self):
        return {
            "name": self.name,
        }