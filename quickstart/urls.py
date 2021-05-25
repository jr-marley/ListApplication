from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('list/', views.locateList, name="api-overview"),
    path('create/', views.locateCreate, name="api-overview")
]
