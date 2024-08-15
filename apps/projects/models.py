from django.db import models
import uuid


class Project(models.Model):
    id = models.UUIDField(primary_key=True,  unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_code = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title