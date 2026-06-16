from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'sales_medium_lassoindex.html', context)
    except Exception as e:
        return render(request, 'sales_medium_lassoerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Sales by Medium Predictor by Lasso.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'TV' : float(request.POST.get('TV')),
            'Radio' : float(request.POST.get('Radio')),
            'Newspaper' : float(request.POST.get('Newspaper'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
                
            result = round(float(model.predict(sample)[0]), 2)  
        context = {
            'result' : result
        }
        return render(request, 'sales_medium_lassoprediction.html', context)
    except Exception as e:
        return render(request, 'sales_medium_lassoerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'sales_medium_lassoabout.html', context)
    except Exception as e:
        return render(request, 'sales_medium_lassoerror.html', {'error': e})

def error(request):
    return render(request, 'sales_medium_lassoerror.html')