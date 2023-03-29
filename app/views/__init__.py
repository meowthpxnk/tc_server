from app import app
from flask import request, send_file
import os

from app.methods.menu import getMenuByLangCode
from app.methods.dishes import getDishInfo


@app.route('/getMenuByLangCode/', methods=['GET'])
def getMenuByLangCodeView():

    try:
        lang_code = request.args["lang_code"]
    except:
        lang_code = "EN"

    print(lang_code)

    menu = getMenuByLangCode(lang_code)

    return {
        "ok": True,
        "data": {
            "menu": menu,
        },
    }


@app.route('/getDishByIdWithLangCode/<id>/', methods=['GET'])
def getDishByIdWithLangCodeView(id):

    try:
        lang_code = request.args["lang_code"]
    except:
        lang_code = "EN"

    dish = getDishInfo(id, lang_code)

    return {
        "ok": True,
        "data": {
            "dish": dish,
        },
    }


@app.route('/images/<directory>/<filename>', methods=['GET'])
def getImage(directory, filename):
    match directory:
        case "categories_icons":
            pass
        case "dishes_images":
            pass
        case _:
            return {"ok": False, "error": "No such directory"}
        
    basedir = os.path.abspath(os.path.dirname(""))
    path = os.path.join(basedir, app.config["STORAGE"], directory, filename)

    try:

        return send_file(path)
    except:
        return {"ok": False, "error": "No such file"}

    return {"ok": False, "error": "Unknown error"}
