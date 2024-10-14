from django.db import models
import uuid

from apps.projects.managers import ProjectQuerySet


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    owner = models.ForeignKey(
        "users.Profile", on_delete=models.SET_NULL, null=True, blank=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_code = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", related_name="tags", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ProjectQuerySet.as_manager()

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (("up", "Up Vote"), ("down", "Down Vote"))

    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    # owner =
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
