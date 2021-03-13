from django.shortcuts import render
import requests

# Create your views here.
def covid19_map(request):
    return render(request,'posts/covid19_map.html')
