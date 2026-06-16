from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'purchasing_power_logistic_regressionindex.html', context)
    except Exception as e:
        return render(request, 'purchasing_power_logistic_regressionerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Purchasing Power Prediction by Logistic Regression.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'Age' : float(request.POST.get('Age')),
            'Income' : float(request.POST.get('Income')),
            'Has_Loan' : int(request.POST.get('Has_Loan'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            result = int(model.predict(sample)[0])

        context = {
            'result' : result
        }
        return render(request, 'purchasing_power_logistic_regressionprediction.html', context)
    except Exception as e:
        return render(request, 'purchasing_power_logistic_regressionerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'purchasing_power_logistic_regressionabout.html', context)
    except Exception as e:
        return render(request, 'purchasing_power_logistic_regressionerror.html', {'error': e})

def error(request):
    return render(request, 'purchasing_power_logistic_regressionerror.html')