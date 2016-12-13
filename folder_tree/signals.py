
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TreeFolder, TreeProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_root(sender, instance=None, created=False, **kwargs):
    """
    Create a tree profile and a root folder to start.

    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        folder = TreeFolder.objects.create(name='root', user=instance, parent=None)
        folder.save()

        profile = TreeProfile.objects.create(user=instance, root_folder=folder)
        profile.save()
