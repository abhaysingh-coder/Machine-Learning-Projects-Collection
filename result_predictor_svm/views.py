from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'result_predictor_svmindex.html', context)
    except Exception as e:
        return render(request, 'result_predictor_svmerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Result Predicter by Support Vector Machine(SVM).pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'StudyHoursPerWeek' : float(request.POST.get('StudyHoursPerWeek')),
            'VideosWatched' : float(request.POST.get('VideosWatched')),
            'AssignmentsCompleted' : float(request.POST.get('AssignmentsCompleted')),
            'ForumActivity' : float(request.POST.get('ForumActivity')),
            'DaysInactive' : float(request.POST.get('DaysInactive'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            result = int(model.predict(sample)[0])  
        context = {
            'result' : result
        }
        return render(request, 'result_predictor_svmprediction.html', context)
    except Exception as e:
        return render(request, 'result_predictor_svmerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'result_predictor_svmabout.html', context)
    except Exception as e:
        return render(request, 'result_predictor_svmerror.html', {'error': e})

def error(request):
    return render(request, 'result_predictor_svmerror.html')