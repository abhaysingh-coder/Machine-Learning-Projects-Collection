from django.urls import path
from weather_prediction_logistic_regression import views

app_name = 'weather_prediction_logistic_regression'

urlpatterns = [
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'),
    path('Prediction', views.prediction, name='Prediction'),
    path('About', views.about, name='About'),
]
