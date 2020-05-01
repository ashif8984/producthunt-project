from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views
from . import contact



urlpatterns = [
    path('signup', views.signup, name='signup'),
    # path('login', views.login, name='login'),
    path('contact/', contact.contact, name='contact'),
    path('logout', views.logout, name='logout'),
    
  ]