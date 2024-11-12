from django.urls import path

from .import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("physician/", views.physician, name="physician"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]