from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex = r"^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    message = "+7(XXX)-XXX-XX-XX",
)

class Users(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, validators=[phone_validator])