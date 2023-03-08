from django.urls import path
from .views import MeshSearchView
from . import views

app_name = 'meshes'

urlpatterns = [
    path('mesh_search/', MeshSearchView.as_view(), name='mesh_search'),
        path('results/', views.results, name='results'),
        path('analyze/', views.analyze, name='analyze'),
        path('report/', views.report, name='report'),
]
