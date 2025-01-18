from django.urls import path
from accounts import auth

urlpatterns = [
    path("login/", auth.user_login, name="login"),
    path("register/", auth.create_accounts, name="accounts"),
]