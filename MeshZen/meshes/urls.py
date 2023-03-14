from django.urls import path
from .views import MeshSearchView
from . import views

app_name = 'meshes'

urlpatterns = [
    path('mesh_search/', MeshSearchView.as_view(), name='mesh_search'),
        path('results/', views.results, name='results'),
        path('visualize/', views.render_mesh, name='render_mesh'),
        path('report/', views.report, name='report'),
]
