from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('subjects', views.subjects, name='subjects'),
    path('online_apply', views.online_apply, name='online_apply')
    
]