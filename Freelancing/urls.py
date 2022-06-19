from django.urls import path, include
from .import views
app_name = 'Freelancing'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"), 
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
]