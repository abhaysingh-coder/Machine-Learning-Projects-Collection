from mainapp import views
from django.contrib import admin
from django.urls import path


app_name = 'mainapp'

urlpatterns = [
    # add app URL patterns here
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'), 
    path('Model', views.model, name='Models'),
    path('About', views.about, name='About'),
]
