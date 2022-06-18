from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/',views.search_results,name='search'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('update/profile/<str:username>/', views.updateprofile, name='updateprofile'),
    path('neighborhoods/', views.neighborhood, name='neighborhood'),
    path('businesses/', views.businesses, name='businesses'),

    
]