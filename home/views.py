from django.shortcuts import render
import requests

# Create your views here. 
# 回傳 html 檔案的值給 urls

def home(request):
    return render(request,'home/home.html')