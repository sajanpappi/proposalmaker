from django.urls import path
from . import views
from .views import index, generate_proposal

urlpatterns = [
    path('', views.index, name='index'),
     path('', index, name='index'),
    path('generate_proposal/', generate_proposal, name='generate_proposal'),
    path('download_proposal/', views.download_proposal, name='download_proposal'),
    
]
