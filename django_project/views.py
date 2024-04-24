from django.http import JsonResponse
import requests
from django.shortcuts import render

def index(request):
  r1 = request.GET.get('https://uselessfacts.jsph.pl/random.json?language=en')
  data = r1.json()
  fact = data['text']
  return render(request, 'templates/index.html', {'fact': fact})