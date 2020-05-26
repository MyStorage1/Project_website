from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import UserModel
from django.dispatch import receiver


@receiver(post_save, sender=User)
def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='user')
        instance.groups.add(group)

        UserModel.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email,
        )
        print('Profile Created!')
