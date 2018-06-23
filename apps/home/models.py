from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, MinLengthValidator


class Contact(models.Model):
    """
    Model to store contacts.
    """
    phone_number_regex_validator = RegexValidator(regex=r'^[0-9]{10}$', message='Invalid Phone Number.')

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10, validators=[phone_number_regex_validator, MinLengthValidator(10)], blank=True, null=True)
    message = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name