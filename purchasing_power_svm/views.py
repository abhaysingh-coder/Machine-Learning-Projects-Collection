from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'purchasing_power_svmindex.html', context)
    except Exception as e:
        return render(request, 'purchasing_power_svmerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Purchasing Power by Support Vector Machine(SVM).pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'Age' : float(request.POST.get('Age')),
            'EstimatedSalary' : float(request.POST.get('EstimatedSalary'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            result = int(model.predict(sample)[0])   
        context = {
            'result' : result
        }
        return render(request, 'purchasing_power_svmprediction.html', context)
    except Exception as e:
        return render(request, 'purchasing_power_svmerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'purchasing_power_svmabout.html', context)
    except Exception as e:
        return render(request, 'purchasing_power_svmerror.html', {'error': e})

def error(request):
    return render(request, 'purchasing_power_svmerror.html')