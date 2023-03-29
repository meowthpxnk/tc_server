from app import db


class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    default_name = db.Column(db.String)
    icon = db.Column(db.String)

    # translates = db.relationship('CategoryTranslate', backref=db.backref(
    #     'category'), lazy=True, cascade="all, delete-orphan")

    

    def __init__(self, default_name):
        self.default_name = default_name

    def __repr__(self) -> str:
        return self.default_name

    def __unicode__(self):
        return self.default_name or ''

    def getInfo(self):
        return {
            "name": self.default_name,
            "id": self.id,
            "icon": "http://localhost:5000/images/categories_icons/" + self.icon,
        }
