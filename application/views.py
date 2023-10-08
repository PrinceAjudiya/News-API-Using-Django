from django.shortcuts import render
import requests
from django.http import HttpResponse, HttpResponseNotFound
import json

# Create your views here.
def index(request):
    try: 
        return render(request, "application/index.html")
    except:
        return HttpResponseNotFound("Sorry!! Page Not Found")

def tesla(request):
    return render(request, "application/tesla.html")

def tesla_output(request):
    try:
        if request.method == 'POST':
            URL = "https://newsapi.org/v2/everything"
            print(request.POST)

            params_from = request.POST.get('from')
            params_api_key = request.POST.get('key')
            PARAMS = {'q':'tesla','from':params_from,'sortBy':'publishedAt','apiKey':params_api_key}

            r = requests.get(url = URL, params = PARAMS)

            data = r.json()

            return render(request, "application/tesla.html", {
                "tesla_output": data['articles']
            })
    except:
        return HttpResponseNotFound("Something is wrong!!")
def business(request):
    return render(request, "application/business.html")

def business_output(request):
    try:
        if request.method == 'POST':
            URL = "https://newsapi.org/v2/top-headlines"
            print(request.POST)

            params_country = request.POST.get('country')
            params_from = request.POST.get('from')            
            params_api_key = request.POST.get('key')

            PARAMS = {'category':'business','country':params_country,'from':params_from,'apiKey':params_api_key}

            r = requests.get(url = URL, params = PARAMS)

            data = r.json()

            return render(request, "application/business.html", {
                "business_output": data['articles']
            })
    except:
        return HttpResponseNotFound("Something is wrong!!")