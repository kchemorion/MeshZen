from django.urls import path
from .views import MeshSearchView
from . import views
from django.shortcuts import render

app_name = 'meshes'

urlpatterns = [
    path('mesh_search/', MeshSearchView.as_view(), name='mesh_search'),
        path('results/', views.results, name='results'),
        path('visualize/', views.visualize, name='visualize'),
        path('report/', views.report, name='report'),
]
