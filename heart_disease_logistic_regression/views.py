from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'heart_disease_logistic_regressionindex.html', context)
    except Exception as e:
        return render(request, 'heart_disease_logistic_regressionerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Heart Disease by Logistic Regression.pkl')
        scaler = load_scaler('Heart Disease by Logistic Regression.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'Age' : float(request.POST.get('Age')),
            'Sex' : float(request.POST.get('Sex')),
            'BP' : float(request.POST.get('BP')),
            'Cholesterol' : float(request.POST.get('Cholesterol')),
            'Max_HR' : float(request.POST.get('Max_HR'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
                
            sample = scaler.transform(sample)
            
            result = round(model.predict(sample)[0], 2)   
        context = {
            'result' : result
        }
        return render(request, 'heart_disease_logistic_regressionprediction.html', context)
    except Exception as e:
        return render(request, 'heart_disease_logistic_regressionerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'heart_disease_logistic_regressionabout.html', context)
    except Exception as e:
        return render(request, 'heart_disease_logistic_regressionerror.html', {'error': e})

def error(request):
    return render(request, 'heart_disease_logistic_regressionerror.html')