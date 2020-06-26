from django.db import models
import datetime
# Create your models here.


class ModelsModel(models.Model):
    model_name = models.TextField()


class PictureModel(models.Model):
    pic_name = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    date = models.DateField(default=datetime.datetime.now)
    model = models.ForeignKey(ModelsModel, on_delete=models.CASCADE)
