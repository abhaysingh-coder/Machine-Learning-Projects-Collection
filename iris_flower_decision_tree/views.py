from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'iris_flower_decision_treeindex.html', context)
    except Exception as e:
        return render(request, 'iris_flower_decision_treeerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Iris Flower Classification by Decision Tree Algorithm.pkl')
        scaler = load_scaler('Iris Flower Classification by Decision Tree Algorithm.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'sepal_length' : float(request.POST.get('sepal-length')),
            'sepal_width' : float(request.POST.get('sepal-width')),
            'petal_length' : float(request.POST.get('petal-length')),
            'petal_width' : float(request.POST.get('petal-width'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
                
            sample = scaler.transform(sample)
            
            prediction = model.predict(sample) [0]
            if prediction == 0:
                result = 'Iris-setosa'

            elif prediction == 1:
                result = 'Iris-versicolor'

            elif prediction == 2:
                result = 'Iris-virginica'

            else:
                result = prediction
        context = {
            'result' : result
        }
        return render(request, 'iris_flower_decision_treeprediction.html', context)
    except Exception as e:
        return render(request, 'iris_flower_decision_treeerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'iris_flower_decision_treeabout.html', context)
    except Exception as e:
        return render(request, 'iris_flower_decision_treeerror.html', {'error': e})

def error(request):
    return render(request, 'iris_flower_decision_treeerror.html')