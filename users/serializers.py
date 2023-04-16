
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

import secrets
import random
from rest_framework.response import Response

class AddCompanySerializer(serializers.Serializer):
    rut = serializers.CharField(required=True)
    company_name = serializers.CharField(required=True)
    is_email_verified = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    user_type = serializers.CharField(required=True)
    latitude = serializers.CharField(required=True)
    longitude = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    is_agreed = serializers.BooleanField(required=True)

class AddIndividualSerializer(serializers.Serializer):
    id_document = serializers.CharField(required=True)
    id_number = serializers.CharField(required=True)
    birth_date = serializers.CharField(required=True)
    first_name =serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    latitude = serializers.CharField(required=True)
    longitude = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    is_agreed = serializers.BooleanField(required=True)
    is_email_verified = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    user_type = serializers.CharField(required=True)

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Duplicate email enter another email")
        return lower_email

    class Meta:
        model = User
        fields = ('email',)


class UserSerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    class Meta:
        model = User
        # title = serializers.CharField(max_length=100)
        # author = serializers.CharField(max_length=100)
        # email = serializers.EmailField(max_length=100)
        # date = serializers .DateTimeField()
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)

    # if Company.objects.filter(is_email_verified=False).exists():
    #     raise serializers.ValidationError("Duplicate email enter another email")

#
class RandomCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)

    def create(self, validated_data):
        validated_data['code'] = str(secrets.randbelow(10000)).zfill(4)
        return super().create(validated_data)



class SendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50, required=True)



    # def generate_code():
    #     return str(random.randint(1000, 9999))
class UserSerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    class Meta:
        model = User
        # title = serializers.CharField(max_length=100)
        # author = serializers.CharField(max_length=100)
        # email = serializers.EmailField(max_length=100)
        # date = serializers .DateTimeField()
        fields = '__all__'


# class ResetpasswordSerializer(serializers.ModelSerializer):
#     # id=serializers.IntegerField()
#     class Meta:
#         model = Resetcode
#         # title = serializers.CharField(max_length=100)
#         # author = serializers.CharField(max_length=100)
#         # email = serializers.EmailField(max_length=100)
#         # date = serializers .DateTimeField()
#         fields = '__all__'
