from django.db import models
from django.contrib.auth.models import User


DOCUMENT_CHOICES = (
    ('passport','passport'),
    ('id_card','id_card'),
)
# Create your models here.
class Company(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=200 )
    company_name = models.CharField(max_length=200)
    is_email_verified = models.BooleanField(default=False)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    is_agreed = models.BooleanField(default=False)

class Individual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_document = models.CharField(max_length=200,choices=DOCUMENT_CHOICES)
    id_number = models.CharField(max_length=200)
    birth_date = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    is_agreed = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

class Resetcode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    is_expired = models.BooleanField(default=False)




