from django.urls import path
from sales_medium_lasso import views

app_name = 'sales_medium_lasso'

urlpatterns = [
    path('', views.index, name='Index'),
    path('Error', views.error, name='Error'),    
    path('Prediction', views.prediction, name='Prediction'),
    path('About', views.about, name='About'),
]
