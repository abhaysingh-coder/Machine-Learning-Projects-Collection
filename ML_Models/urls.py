"""
URL configuration for ML_Models project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.mainappurls')),
    path('car-price/', include('car_price_prediction.car_price_predictionurls')),
    path('customer-purchase/', include('customer_purchase_prediction.customer_purchase_predictionurls')),
    path('employee-attrition/', include('employee_attrition_prediction.employee_attrition_predictionurls')),
    path('heart-disease-logistic/', include('heart_disease_logistic_regression.heart_disease_logistic_regressionurls')),
    path('heart-disease-svm/', include('heart_disease_svm.heart_disease_svmurls')),
    path('iris-decision-tree/', include('iris_flower_decision_tree.iris_flower_decision_treeurls')),
    path('iris-knn/', include('iris_flower_knn.iris_flower_knnurls')),
    path('loan-decision-tree/', include('loan_approval_decision_tree.loan_approval_decision_treeurls')),
    path('loan-random-forest/', include('loan_approval_random_forest.loan_approval_random_foresturls')),
    path('placement-predictor/', include('placement_predictor_decision_tree.placement_predictor_decision_treeurls')),
    path('purchasing-power-svm/', include('purchasing_power_svm.purchasing_power_svmurls')),
    path('purchasing-power-logistic/', include('purchasing_power_logistic_regression.purchasing_power_logistic_regressionurls')),
    path('result-predictor-svm/', include('result_predictor_svm.result_predictor_svmurls')),
    path('sales-medium-lasso/', include('sales_medium_lasso.sales_medium_lassourls')),
    path('sales-category-knn/', include('sales_category_knn.sales_category_knnurls')),
    path('sports-prediction-knn/', include('sports_prediction_knn.sports_prediction_knnurls')),
    path('weather-prediction-logistic/', include('weather_prediction_logistic_regression.weather_prediction_logistic_regressionurls')),
]
