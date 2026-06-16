from django.urls import path
from loan_approval_decision_tree import views

app_name = 'loan_approval_decision_tree'

urlpatterns = [
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'),
    path('Prediction', views.prediction, name='Prediction'),
    path('About', views.about, name='About'),
]
