from app import db
from app.models.Language import Language

def createLanguage(lang_code):
    language = Language(lang_code)
    
    db.session.add(language)
    db.session.commit()

def findLanguageById(id):
    ...

def findLanguageByLangCode(lang_code):
    language = db.session.query(Language).filter(Language.lang_code == lang_code).first()

    if not language:
        raise Exception
    
    return language