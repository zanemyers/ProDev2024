from django.urls import path
from apps.users import views

urlpatterns = [
    path("", views.ProfilesView, name="profiles"),
    path("profile/<str:pk>/", views.UserProfileView, name="user-profile"),
]
