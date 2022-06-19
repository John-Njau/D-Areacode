from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('home/<int:neighborhood_id>/', views.home, name='home'),
    path('search/',views.search_results,name='search'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('other/profile/<str:username>/', views.user_profile, name='user_profile'),
    path('update/profile/<str:username>/', views.updateprofile, name='updateprofile'),
    path('neighborhoods/', views.neighborhood, name='neighborhood'),
    path('businesses/<int:neighborhood_id>/', views.businesses, name='businesses'),
    path('social_amenities/<int:neighborhood_id>/', views.social_amenities, name='social_amenities'),
    
]