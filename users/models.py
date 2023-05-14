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
    id_document = models.CharField(max_length=10,choices=DOCUMENT_CHOICES)
    birth_date = models.DateField(auto_now=False,null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    is_agreed = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    verification_badge = models.CharField(default="not_applied",max_length=50)
    profile_pic = models.ImageField(upload_to='profile images',null=True)
    document_no = models.CharField(max_length=200,null=True)


class Resetcode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    is_expired = models.BooleanField(default=False)


class VerificationInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=True)
    document_type = models.CharField(max_length=200)
    front_pic=models.ImageField(upload_to='images')
    back_pic=models.ImageField(upload_to='images')
    user_with_document_pic=models.ImageField(upload_to='images',null=True)
    is_verified = models.BooleanField(default=False)


class UpdateEmail(models.Model):

    token = models.CharField(max_length=200,null=False,unique=True)
    email_address = models.CharField(max_length=200,null=False)












