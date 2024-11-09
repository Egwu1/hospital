from django.urls import path
app_name = "core"
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("physician/", views.physician, name="physician"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]