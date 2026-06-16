from django.urls import path
from iris_flower_knn import views

app_name = 'iris_flower_knn'

urlpatterns = [
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'),
    path('Prediction', views.prediction, name='Prediction'),
    path('About', views.about, name='About'),
]
