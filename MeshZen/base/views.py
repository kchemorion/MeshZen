from django.shortcuts import render

def home(request):
    return render(request, 'base/landing.html')

def about(request):
    return render(request, 'base/about.html')

def documentation(request):
    return render(request, 'base/documentation.html')

def contact(request):
    return render(request, 'base/contact.html')

def features(request):
    return render(request, 'base/features.html')

def download(request):
    return render(request, 'base/download.html')