from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # nickname = models.CharField(max_length=15, null=False, unique=True)
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    avatar = models.CharField(max_length=500)
    date_joined = models.DateTimeField(auto_now_add=True)

    # REQUIRED_FIELDS = ['username', 'nickname']
    REQUIRED_FIELDS = ['username']

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

# Create your models here.
