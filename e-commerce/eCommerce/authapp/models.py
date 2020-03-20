from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    phone =  models.CharField(max_length=100)
    username = models.CharField(max_length=25, default='customer', unique=True)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'phone', 'first_name']

    def get_username(self):
        return self.username

    # admin
    # pass: 87654321a


