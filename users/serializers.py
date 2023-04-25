
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



class AddCompanySerializer(serializers.Serializer):
    rut = serializers.CharField(required=True)
    company_name = serializers.CharField(required=True)
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

    class Meta:
        model = User

        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)

#

class SendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50, required=True)




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class  ChangePasswordSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(required=True)
    is_expired = serializers.CharField(required=True)

class getcompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company

        fields = '__all__'

class GetIndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = Individual

        fields = '__all__'


class AddVerificationBadgeSerializer(serializers.Serializer):
    document_type = serializers.CharField(required=True)
    front_pic = serializers.ImageField(required=True)
    back_pic = serializers.ImageField(required=False)



    def validate(self, data):
        """
        Check document_type is valid
        """
        if data['document_type'] not in ["passport", "id_card"]:
            raise serializers.ValidationError("document_type must be id_card or passport")
        return data

class VerificationBadgeResponseSerializer(serializers.Serializer):
    document_type = serializers.CharField(required=True)
    front_pic = serializers.ImageField(required=True)
    back_pic = serializers.ImageField(required=False)
    is_verified=serializers.BooleanField(required=True)

