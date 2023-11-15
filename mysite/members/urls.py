from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("login_user", views.login_user, name="login"),
    path("signup/",views.signup, name="signup"),
    path("logout_view", views.logout_view, name="logout"),
]