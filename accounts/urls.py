from django.urls import path, include
from . import views
from accounts import views as user_views

from django.contrib.auth import views as auth_views
#from . import contact



urlpatterns = [
    #path('signup', views.signup, name='signup'),
    path('register/', user_views.register, name='register'),

    # path('login', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login2.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout' ),
    # path('login', views.loginform, name='loginform'),
    # path('logout', user_views.logout, name='logout'),
    
  ]