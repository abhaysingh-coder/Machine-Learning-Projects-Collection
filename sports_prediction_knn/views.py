from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'sports_prediction_knnindex.html', context)
    except Exception as e:
        return render(request, 'sports_prediction_knnerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Sports Prediction by KNN.pkl')
        encoder = load_encoder('Sports Prediction by KNN.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'Age' : float(request.POST.get('Age')),
            'Gender' : encoder.transform([request.POST.get('Gender')])[0]
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            result = model.predict(sample)[0]     
        context = {
            'result' : result
        }
        return render(request, 'sports_prediction_knnprediction.html', context)
    except Exception as e:
        return render(request, 'sports_prediction_knnerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'sports_prediction_knnabout.html', context)
    except Exception as e:
        return render(request, 'sports_prediction_knnerror.html', {'error': e})

def error(request):
    return render(request, 'sports_prediction_knnerror.html')