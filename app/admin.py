from flask_admin.contrib.sqla import ModelView
from slugify import slugify


class SetSlugField(ModelView):

    def on_model_change(self, form, model, is_created):
        model.slug = slugify(model.name)
        print(form.slug)
        print(model.slug)
        print(is_created)
        return super().on_model_change(form, model, is_created)