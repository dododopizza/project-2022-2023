from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, max_length=16)
    age = models.TextField(blank=False, null=True)
    photo = models.ImageField(upload_to='users/avatars/', blank=True)
    role = models.TextField(blank=False, null=True)
    country = models.TextField(blank=False, null=True)
    city = models.TextField(blank=False, null=True)
    email = models.TextField(blank=False, null=True)
    tools = models.TextField(blank=False, null=True)
    interest = models.TextField(blank=False, null=True)
    work_time = models.TextField(blank=False, null=True)
    GMT = models.TextField(blank=False, null=True)
    date_reg = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Project(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.TextField(blank=False, null=True)
    name_project = models.TextField(blank=False, null=True)
    date = models.TextField(blank=True, null=True)
    who = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
