from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('neworder', views.neworder, name="neworder"),
    path('createpizza', views.createpizza, name="createpizza"),
    path('details', views.details, name="details"),
    path('orderdetails', views.orderdetails, name="orderdetails"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]