from django.shortcuts import render

# Create your views here.
def index(request):
    try:
        return render(request, 'mainappindex.html')
    except Exception as e:
        return render(request, 'mainapperror.html', {'error':e})

def model(request):
    try:
        return render(request, 'mainappmodel.html')
    except Exception as e:
        return render(request, 'mainapperror.html', {'error':e})

def about(request):
    try:
        return render(request, 'mainappabout.html')
    except Exception as e:
        return render(request, 'mainapperror.html', {'error':e})

def error(request):
    return render(request, 'mainapperror.html')
