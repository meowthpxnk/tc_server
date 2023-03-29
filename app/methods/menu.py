from app import db
from app.models.Category import Category
from app.models.Dish import Dish
from .languages import findLanguageByLangCode
from .dishes import findDishTranslate
from .categories import findCategoryTranslate


def getMenuByLangCode(lang_code):
    dishes = db.session.query(Dish).all()
    categories = db.session.query(Category).all()
    try:
        language = findLanguageByLangCode(lang_code)
    except:
        language = findLanguageByLangCode("EN")

    dump = {
        "dishes": [],
        "categories": [],
    }

    for dish in dishes:

        object = dish.getInfo()

        try:
            translate = findDishTranslate(dish.id, language.id)
        except:
            dump["dishes"].append(object)
            continue

        object.update(translate.getSemiInfo())

        dump["dishes"].append(object)

    for category in categories:
        object = category.getInfo()

        try:
            translate = findCategoryTranslate(category.id, language.id)
        except:
            dump["categories"].append(object)
            continue

        object.update(translate.getInfo())

        dump["categories"].append(object)

    return dump
