from django.db import models
from django.core.validators import MinLengthValidator

class UserModel(models.Model):
    username = models.CharField(max_length=25, unique=True, validators=[MinLengthValidator(limit_value=5)])
    password = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(limit_value=5)])
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)