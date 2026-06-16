from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'sales_category_knnindex.html', context)
    except Exception as e:
        return render(request, 'sales_category_knnerror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Sales Category by KNN.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
            'Price' : float(request.POST.get('Price')),
            'Discount' : float(request.POST.get('Discount')),
            'AdSpend' : float(request.POST.get('AdSpend')),
            'Visitors' : float(request.POST.get('Visitors'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            result = int(model.predict(sample)[0])   
        context = {
            'result' : result
        }
        return render(request, 'sales_category_knnprediction.html', context)
    except Exception as e:
        return render(request, 'sales_category_knnerror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'sales_category_knnabout.html', context)
    except Exception as e:
        return render(request, 'sales_category_knnerror.html', {'error': e})

def error(request):
    return render(request, 'sales_category_knnerror.html')