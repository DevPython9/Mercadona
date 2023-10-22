# from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1>Bienvenue sur Mercado Store </h1>")

def index(request):
    return render(request, "index.html")