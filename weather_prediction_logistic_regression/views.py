from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'weather_prediction_logistic_regressionindex.html', context)
    except Exception as e:
        return render(request, 'weather_prediction_logistic_regressionerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Weather Prediction by Logistic Regression.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
                'precipitation': float(request.POST.get('precipitation')),
                'temp_max': float(request.POST.get('temp_max')),
                'temp_min': float(request.POST.get('temp_min')),
                'wind': float(request.POST.get('wind'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            result = model.predict(sample)[0]  
        context = {
            'result' : result
        }
        return render(request, 'weather_prediction_logistic_regressionprediction.html', context)
    except Exception as e:
        return render(request, 'weather_prediction_logistic_regressionerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'weather_prediction_logistic_regressionabout.html', context)
    except Exception as e:
        return render(request, 'weather_prediction_logistic_regressionerror.html', {'error': e})

def error(request):
    return render(request, 'weather_prediction_logistic_regressionerror.html')