from django.shortcuts import render, HttpResponse

def homedef(request):
    return render(request, 'core/home.html')