from django.urls import path
from placement_predictor_decision_tree import views

app_name = 'placement_predictor_decision_tree'

urlpatterns = [
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'),
    path('Prediction', views.prediction, name='Prediction'),
    path('About', views.about, name='About'),
]
