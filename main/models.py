from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Profile(models.Model):
    hometown = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    user = models.ForeignKey(
        User, related_name='profile',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}_profile'.format(self.user.username)
