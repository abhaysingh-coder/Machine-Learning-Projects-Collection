from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.

def index(request):
    try:
        context = {}
        return render(request, 'car_price_predictionindex.html', context)
    except Exception as e:
        return render(request, 'car_price_predictionerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Car Price Prediction by Simple Linear Regression.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'Car_Age' : request.POST.get('Car_Age'),
            'KM_Driven' : request.POST.get('KM_Driven'),
            'Fuel_Type' : request.POST.get('Fuel_Type'),
            'Owner_Type' : request.POST.get('Owner_Type'),
            'Mileage' : request.POST.get('Mileage'),
            'Engine_Size' : request.POST.get('Engine_Size')
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            result = round(model.predict(sample)[0], 2)   
        context = {
            'result' : result
        }
        return render(request, 'car_price_predictionprediction.html', context)
    except Exception as e:
        return render(request, 'car_price_predictionerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'car_price_predictionabout.html', context)
    except Exception as e:
        return render(request, 'car_price_predictionerror.html', {'error': e})

def error(request):
    return render(request, 'car_price_predictionerror.html')