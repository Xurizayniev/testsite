from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserModel(BaseUserManager):
    pass


class UserModel(AbstractUser):
    phone = models.CharField(max_length=13)
    user_image = models.ImageField(upload_to='user_img/')