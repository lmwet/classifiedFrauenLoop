from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='public_profiles/static')
    skills = models.CharField(max_length=250, blank=True)
    languages = models.CharField(max_length=250, blank=True)
    likes = models.CharField(max_length=250, blank=True)
    dislikes = models.CharField(max_length=250, blank=True)
    github = models.CharField(max_length=250, blank=True)

 # now need to edit forms, then add to the template
    def __str__(self):
        return f'{self.user.username} Profile'
