from django.shortcuts import render

# Create your views here.

def corepage(request):
    return render(request, 'core/home.html')
