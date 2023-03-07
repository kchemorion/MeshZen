from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('documentation/', views.documentation, name='documentation'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('download/', views.contact, name='download'),
]
