from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'customer_purchase_predictionindex.html', context)
    except Exception as e:
        return render(request, 'customer_purchase_predictionerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Customer Purchase Prediction by Logistic Regression.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'Age' : request.POST.get('Age'),
            'EstimatedSalary' : request.POST.get('EstimatedSalary')
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            result = round(model.predict(sample)[0], 2)   
        context = {
            'result' : result
        }
        return render(request, 'customer_purchase_predictionprediction.html', context)
    except Exception as e:
        return render(request, 'customer_purchase_predictionerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'customer_purchase_predictionabout.html', context)
    except Exception as e:
        return render(request, 'customer_purchase_predictionerror.html', {'error': e})

def error(request):
    return render(request, 'customer_purchase_predictionerror.html')