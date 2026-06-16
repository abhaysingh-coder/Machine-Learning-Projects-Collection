from django.shortcuts import render
from function import *
import pandas as pd


# Create your views here.
def index(request):
    try:
        context = {}
        return render(request, 'loan_approval_random_forestindex.html', context)
    except Exception as e:
        return render(request, 'loan_approval_random_foresterror.html', {'error': e})

def prediction(request):
    try:
        model = load_prediction('Loan by Random Forest.pkl')
        result = None
        if request.method == 'POST':
            sample_dict = {
                'Age': float(request.POST.get('Age')),
                'Income': float(request.POST.get('Income')),
                'CreditScore': float(request.POST.get('CreditScore')),
                'Experience': float(request.POST.get('Experience')),
                'LoanAmount': float(request.POST.get('LoanAmount'))
            }

            sample = pd.DataFrame([sample_dict])

            for col_name in sample.columns:
                if sample[col_name].iloc[0] in [None, '']:
                    raise ValueError(f'{col_name} is empty')
            
            prediction = model.predict(sample)[0] 
            if prediction == 1:
                result = "Approved"

            elif prediction == 0:
                result = "Rejected"

            else:
                result = str(prediction)   
        context = {
            'result' : result
        }
        return render(request, 'loan_approval_random_forestprediction.html', context)
    except Exception as e:
        return render(request, 'loan_approval_random_foresterror.html', {'error': e})
    
def about(request):
    try:
        context = {}
        return render(request, 'loan_approval_random_forestabout.html', context)
    except Exception as e:
        return render(request, 'loan_approval_random_foresterror.html', {'error': e})

def error(request):
    return render(request, 'loan_approval_random_foresterror.html')