from flask_admin import form
from flask_admin.contrib.sqla import ModelView
import random
import os
from app import admin, db, app

from app.models.Category import Category
from app.models.CategoryTranslate import CategoryTranslate
from app.models.Dish import Dish
from app.models.DishTranslate import DishTranslate
from app.models.Language import Language


class CategoryView(ModelView):
    form_extra_fields = {
        'file': form.FileUploadField('file')
    }

    def _change_path_data(self, _form):
        try:
            storage_file = _form.file.data

            if storage_file is not None:
                ...
                hash = random.getrandbits(128)
                ext = storage_file.filename.split('.')[-1]
                path = '%s.%s' % (hash, ext)

                storage_file.save(
                    os.path.join(app.config['STORAGE'],
                                 'categories_icons', path)
                )

                _form.icon.data = path

                del _form.file

        except Exception as ex:
            pass

        return _form

    def edit_form(self, obj=None):
        return self._change_path_data(
            super(CategoryView, self).edit_form(obj)
        )

    def create_form(self, obj=None):
        return self._change_path_data(
            super(CategoryView, self).create_form(obj)
        )

    create_modal = True


class CategoryTranslateView(ModelView):
    column_list = ['category', 'language', 'name']
    form_columns = ['category', 'language', 'name']

    create_modal = True


class DishView(ModelView):
    # column_list = ['category', 'default_name', 'price']
    # form_columns = ['category', 'default_name', 'price']

    form_extra_fields = {
        'file': form.FileUploadField('file')
    }

    def _change_path_data(self, _form):
        try:
            storage_file = _form.file.data

            if storage_file is not None:
                hash = random.getrandbits(128)
                ext = storage_file.filename.split('.')[-1]
                path = '%s.%s' % (hash, ext)

                storage_file.save(
                    os.path.join(app.config['STORAGE'], 'dishes_images', path)
                )

                _form.image.data = path

                del _form.file

        except Exception as ex:
            pass

        return _form

    create_modal = True

    def edit_form(self, obj=None):
        return self._change_path_data(
            super(DishView, self).edit_form(obj)
        )

    def create_form(self, obj=None):
        return self._change_path_data(
            super(DishView, self).create_form(obj)
        )


class DishTranslateView(ModelView):
    # column_list = ['language', 'dish', 'name', 'portion', 'ingredients', 'description']
    # form_columns = ['language', 'dish', 'name', 'portion', 'ingredients', 'description']

    create_modal = True


class LanguageView(ModelView):
    column_list = ['lang_code']
    form_columns = ['lang_code']


admin.add_view(CategoryView(Category,
               db.session, category="Categories"))
admin.add_view(CategoryTranslateView(CategoryTranslate,
               db.session, category="Categories", name="Translates"))
admin.add_view(DishView(Dish, db.session, category="Dishes"))
admin.add_view(DishTranslateView(DishTranslate, db.session,
               category="Dishes", name="Translates"))
admin.add_view(LanguageView(Language, db.session))
