from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import requests, json
# Create your views here.

def index (request):
  # call the api with get request
  response = requests.get('https://swapi.dev/api/films/').json()  
  return render(request, "index.html", {'response':response})


def crawl(request,pk):        
    return render(request, "crawl.html",  {'id':pk})  


def crawl_reverse(request,pk):    
  return render(request, "crawl-reverse.html",  {'id':pk})