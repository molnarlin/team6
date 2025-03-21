from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_list, name='about_list'),
    path('<int:pk>/', views.about_detail, name='about_detail'),
]