from app import db
from app.models.Dish import Dish
from app.models.DishTranslate import DishTranslate

from .categories import findCategoryById
from .languages import findLanguageByLangCode


def findDishById(id):
    dish = db.session.query(Dish).filter(Dish.id == id).first()

    if not dish:
        raise Exception

    return dish


def findDishTranslate(dish_id, language_id):
    dish_translate = db.session.query(DishTranslate).filter(
        DishTranslate.dish_id == dish_id, DishTranslate.language_id == language_id).first()

    if not dish_translate:
        raise Exception

    return dish_translate


def createDish(name, price, category_id):

    category = findCategoryById(category_id)

    dish = Dish(name, price, category.id)

    db.session.add(dish)
    db.session.commit()


def createDishTranslate(id, lang_code, name, portion, ingredients, description):
    dish = findDishById(id)
    language = findLanguageByLangCode(lang_code)

    dish_translate = DishTranslate(
        name=name,
        portion=portion,
        ingredients=ingredients,
        description=description,

        dish_id=dish.id,
        language_id=language.id
    )

    db.session.add(dish_translate)
    db.session.commit()


def getDishInfo(id, lang_code):
    dish = findDishById(id)
    try:
        language = findLanguageByLangCode(lang_code)
        translate = findDishTranslate(dish.id, language.id)
    except:
        language = findLanguageByLangCode("EN")
        translate = findDishTranslate(dish.id, language.id)

    return {
        "name": translate.name,
        "description": translate.description,
        "portion": translate.portion,
        "ingredients": translate.ingredients,

        "price": dish.price,
        "image": "http://localhost:5000/images/dishes_images/" + dish.image,
    }
