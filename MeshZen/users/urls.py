from django.urls import path
from . import views

urlpatterns = [
    path('login_with_zenodo/', views.login_with_zenodo, name='login_with_zenodo'),
    path('callback_from_zenodo/', views.callback_from_zenodo, name='callback_from_zenodo'),
]
