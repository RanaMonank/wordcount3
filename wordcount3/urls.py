

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="Home"),
    path('count/', views.count, name="count"),
    path('Help/', views.Help, name="Help"),
    path('About/', views.About, name="About"),
]
