from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')