from django.urls import path
from apps.projects import views

urlpatterns = [
    path("", views.ProjectsListView, name="projects"),
    path("project/<str:pk>", views.SingleProjectView, name="project"),
    path("create-project", views.CreateProjectView, name="create-project"),
    path("update-project/<str:pk>", views.UpdateProjectView, name="update-project"),
    path("delete-project/<str:pk>", views.DeleteProjectView, name="delete-project"),
]
