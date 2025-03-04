from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('auto/<int:blog_id>/', views.auto, name='auto'),
    path('check/', views.blog_author, name='blogs'),
    path('first/', views.index, name='first'),
]
