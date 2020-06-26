from django.urls import path

from . import views

urlpatterns = [
    path('', views.information),
    path('generation/', views.generation),
    path('training/', views.training),
    path('algorithm/', views.algorithm),
    path('pictures/', views.pictures),
    path('save/', views.save_pic)
]
