from django.urls import path
from .views import MeshSearchView

app_name = 'meshes'

urlpatterns = [
    path('mesh_search/', MeshSearchView.as_view(), name='mesh_search'),
]
