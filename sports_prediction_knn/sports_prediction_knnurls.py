from django.urls import path
from sports_prediction_knn import views

app_name = 'sports_prediction_knn'

urlpatterns = [
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'),    
    path('Prediction', views.prediction, name='Prediction'),
    path('About', views.about, name='About'),
]
