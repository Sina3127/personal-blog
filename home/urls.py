from django.contrib import admin
from django.urls import path

from home.views import Home

urlpatterns = [
    path('home/', Home.as_view(), name='home')
]