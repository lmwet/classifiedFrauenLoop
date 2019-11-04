from django.db.models.signals import post_save #when a user gets saved
from django.contrib.auth.models import User #this is why we need the User as well
from django.dispatch import receiver # function that gets this signals and performs a task
from .models import Profile #because we'll create a profile in our function

@receiver(post_save, sender=User) #when a user is saved create this signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #when the user object is updated
def save_profile(sender, instance, **kwargs):
    instance.profile.save()