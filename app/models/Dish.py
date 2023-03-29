from app import db

class Dish(db.Model):

    __tablename__ = 'dishes'

    id = db.Column(db.Integer, primary_key=True)
    default_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    image = db.Column(db.String)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('dishes', lazy='dynamic'))

    def __init__(self, default_name, price, category_id):
        self.default_name = default_name
        self.price = price
        self.category_id = category_id

    def getInfo(self):
        return {
            "name": self.default_name,
            "id": self.id,
            "price": self.price,
            "category_id": self.category.id,
            "image": "http://localhost:5000/images/dishes_images/" + self.image
        }
    
    def __repr__(self):
        return self.default_name