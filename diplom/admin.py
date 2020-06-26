from django.contrib import admin

# Register your models here.
from .models import ModelsModel, PictureModel

admin.site.register(ModelsModel)
admin.site.register(PictureModel)
