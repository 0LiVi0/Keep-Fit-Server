from restAccount import views
from django.urls import path
from rest_framework.authtoken import views as authviews

urlpatterns = [
	path('register/', views.Register.as_view()),
	path('api-token-auth/', authviews.obtain_auth_token),
]