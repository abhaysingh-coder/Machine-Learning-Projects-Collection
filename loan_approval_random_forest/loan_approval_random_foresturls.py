from django.urls import path
from loan_approval_random_forest import views

app_name = 'loan_approval_random_forest'

urlpatterns = [
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'),
    path('Prediction', views.prediction, name='Prediction'),
    path('About', views.about, name='About'),
]
