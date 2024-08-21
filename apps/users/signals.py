from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from apps.users.models import Profile


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    print("createProfile")
    if created:
        user = instance
        Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
        )


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    try:
        if instance.user:
            instance.user.delete()
    except ObjectDoesNotExist:
        # The user does not exist, so do nothing
        pass
