from app import db
from app.models.Category import Category
from app.models.CategoryTranslate import CategoryTranslate
from .languages import findLanguageByLangCode


def findCategoryById(id):
    category = db.session.query(Category).filter(Category.id == id).first()

    if not category:
        raise Exception("Not found category by ID")

    return category


def createCategory(name):
    category = Category(name)

    db.session.add(category)
    db.session.commit()


def findCategoryTranslate(category_id, language_id):

    print(f"{category_id=}")
    print(f"{language_id=}")

    category_translate = db.session.query(CategoryTranslate).filter(
        CategoryTranslate.category_id == category_id, CategoryTranslate.language_id == language_id).first()
    
    print(category_translate)

    if not category_translate:
        raise Exception

    return category_translate


def createCategoryTranslate(id, lang_code, name):
    category = findCategoryById(id)
    language = findLanguageByLangCode(lang_code)

    category_translate = CategoryTranslate(
        name=name,

        category_id=category.id,
        language_id=language.id
    )

    db.session.add(category_translate)
    db.session.commit()


def getCategoryInfo(id, lang_code):
    category = findCategoryById(id)
    
    try:
        language = findLanguageByLangCode(lang_code)
        translate = findCategoryTranslate(category.id, language.id)
    except:
        language = findLanguageByLangCode("EN")
        translate = findCategoryTranslate(category.id, language.id)

    return {
        "name": translate.name,
    }
