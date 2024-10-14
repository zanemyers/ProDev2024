from django.urls import path
from apps.users import views

urlpatterns = [
    path("login/", views.LoginView, name="login"),
    path("logout/", views.LogoutView, name="logout"),
    path("register/", views.RegisterView, name="register"),
    path("", views.ProfilesView, name="profiles"),
    path("profile/<str:pk>/", views.UserProfileView, name="user-profile"),
    path("account/", views.UserAccountView, name="account"),
    path("edit-account/", views.EditAccountView, name="edit-account"),
    path("create-skill/", views.CreateSkillView, name="create-skill"),
    path("update-skill/<str:pk>/", views.UpdateSkillView, name="update-skill"),
    path("delete-skill/<str:pk>/", views.DeleteSkillView, name="delete-skill"),
]
