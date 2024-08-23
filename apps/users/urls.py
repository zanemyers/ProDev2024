from django.urls import path
from apps.users import views

urlpatterns = [
    path("login/", views.LoginView, name="login"),
    path("logout/", views.LogoutView, name="logout"),
    path("register/", views.RegisterView, name="register"),
    path("", views.ProfilesView, name="profiles"),
    path("profile/<str:pk>/", views.UserProfileView, name="user-profile"),
]
