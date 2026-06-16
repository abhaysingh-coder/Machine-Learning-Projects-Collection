from django.urls import path
from purchasing_power_svm import views

app_name = 'purchasing_power_svm'

urlpatterns = [
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'),
    path('Prediction', views.prediction, name='Prediction'),
    path('About', views.about, name='About'),
]
