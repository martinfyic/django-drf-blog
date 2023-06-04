from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='user_set_custom')
    user_permissions = models.ManyToManyField(
        Permission, related_name='user_set_custom')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
