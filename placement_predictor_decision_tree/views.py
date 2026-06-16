from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'placement_predictor_decision_treeindex.html', context)
    except Exception as e:
        return render(request, 'placement_predictor_decision_treeerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Placement Predictor by Decision Tree Algorithm.pkl')
        scaler = load_scaler('Placement Predictor by Decision Tree Algorithm.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'Hours_Studied' : float(request.POST.get('Hours_Studied')),
            'Attendance' : float(request.POST.get('Attendance')),
            'Previous_Score' : float(request.POST.get('Previous_Score'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
                
            sample = scaler.transform(sample)
            
            prediction = model.predict(sample)[0]

            if prediction == 1:
                result = "Placed"
            else:
                result = "Not Placed"
  
        context = {
            'result' : result
        }
        return render(request, 'placement_predictor_decision_treeprediction.html', context)
    except Exception as e:
        return render(request, 'placement_predictor_decision_treeerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'placement_predictor_decision_treeabout.html', context)
    except Exception as e:
        return render(request, 'placement_predictor_decision_treeerror.html', {'error': e})

def error(request):
    return render(request, 'placement_predictor_decision_treeerror.html')