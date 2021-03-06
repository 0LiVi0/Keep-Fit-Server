from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('login/', auth_views.LoginView.as_view(template_name='myaccount/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='myAccount/logout.html')),
    # TODO: add path 
    path('register/', views.register),
]