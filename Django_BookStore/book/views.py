from django.shortcuts import render

def home(request):
    return render(request, 'book/index.html')

def about(request):
    return render(request, 'book/about.html')