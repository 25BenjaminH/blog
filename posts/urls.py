from django.urls import path
from . import views

# 網頁路徑 網頁在 views 裡的功能 名稱
urlpatterns = [
    path('COVID19_Map/', views.covid19_map, name = "covid19_map"),
]