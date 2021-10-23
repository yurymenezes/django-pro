from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class User(AbstractUser):

    bio = models.TextField(blank=True)
    user_imagem = models.ImageField(upload_to='Users/', blank=True)
