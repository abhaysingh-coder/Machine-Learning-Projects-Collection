from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'employee_attrition_predictionindex.html', context)
    except Exception as e:
        return render(request, 'employee_attrition_predictionerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Employee Attrition Prediction by Random Forest.pkl')
        encoder = load_encoder('Employee Attrition Prediction by Random Forest.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'Age' : float(request.POST.get('Age')),
            'Salary' : float(request.POST.get('Salary')),
            'JobSatisfaction' : float(request.POST.get('JobSatisfaction')),
            'WorkHours' : float(request.POST.get('WorkHours')),
            'Experience' : float(request.POST.get('Experience')),
            'Department' : encoder.transform([request.POST.get('Department')])[0]
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            result = round(model.predict(sample)[0], 2)   
        context = {
            'result' : result
        }
        return render(request, 'employee_attrition_predictionprediction.html', context)
    except Exception as e:
        return render(request, 'employee_attrition_predictionerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'employee_attrition_predictionabout.html', context)
    except Exception as e:
        return render(request, 'employee_attrition_predictionerror.html', {'error': e})

def error(request):
    return render(request, 'employee_attrition_predictionerror.html')
