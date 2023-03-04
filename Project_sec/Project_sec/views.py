from django.http import HttpResponse
from django.shortcuts import render

# def homepage(request):
#     return render (request,"index.html")

def resume(request):
    return render(request,"resume.html")