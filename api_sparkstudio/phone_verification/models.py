from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^1?\d{9,15}$', message="Invalid Phone Number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False, null=True) 
    def __str__(self):
        return str(self.username)