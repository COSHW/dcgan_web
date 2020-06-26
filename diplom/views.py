from django.shortcuts import render, redirect
import main
import random
import os
from .models import ModelsModel, PictureModel
# Create your views here.


def information(request):
    return render(request, 'information.html')


def generation(request):
    if request.method == "POST":
        examples_to_generate = request.POST.get('num_of_examples')
        model_file = request.POST.get('model_name')
        seed = request.POST.get('seed_list')
        image = main.generate_random(random.randint(10000000, 99999999), examples_to_generate, model_file, seed)
        models = os.listdir('models')
        return render(request, 'generation.html', {'img_path': image, 'models': zip(range(len(models)), models), 'created':True, 'model': model_file})
    models = os.listdir('models')
    return render(request, 'generation.html', {'models': zip(range(len(models)), models)})


def training(request):
    return render(request, 'training.html')


def algorithm(request):
    return render(request, 'algorithm.html')


def save_pic(request):
    if request.method == "POST":
        pic_name = request.POST.get('pic_name')
        img_path = request.POST.get('img_path')
        model = request.POST.get('model')
        new_row = PictureModel(pic_name=pic_name, file_name=img_path, model=ModelsModel.objects.get(model_name=model))
        new_row.save()
    return redirect('/pictures/')


def pictures(request):
    data = PictureModel.objects.all()
    return render(request, 'pics.html', {'pics': data})
