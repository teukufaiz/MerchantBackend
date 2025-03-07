from django.urls import path
from .views import *

urlpatterns = [
    # path('logout/', views.logout_view, name='logout'),
    path('register', register, name='register'),
    path('login', login, name='login'),
]