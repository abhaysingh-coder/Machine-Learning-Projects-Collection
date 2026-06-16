from django.urls import path
from employee_attrition_prediction import views

app_name = 'employee_attrition_prediction'

urlpatterns = [
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'),
    path('Prediction', views.prediction, name='Prediction'),
    path('About', views.about, name='About'),
]
