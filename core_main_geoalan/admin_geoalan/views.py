from django.shortcuts import render


def home(request):

    context = {
        'message': "hola a todos"
    }
    
    return render(request, 'index.html', context)

# Create your views here.
