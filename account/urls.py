from django.urls import path
from account import views

urlpatterns = [
    path("register",views.RegisterUser.as_view(),name="register"),
    path("login",views.LoginUser.as_view(),name="login"),
    path("dashboard",views.DashboardView.as_view(),name="dashboard"),
]