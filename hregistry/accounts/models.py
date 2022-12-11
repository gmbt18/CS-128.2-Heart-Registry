from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Enter user models here
class AuthUser(AbstractUser):
    USER_TYPE_CHOICES = {
        (1, 'Nurse'),
        (2, 'Doctor'),
        (3, 'Medtech'),
        (4, 'Radtech'),
    }

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,null=True)

