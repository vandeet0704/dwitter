from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
]