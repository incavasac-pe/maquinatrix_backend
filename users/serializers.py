from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date


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
    birth_date = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    latitude = serializers.CharField(required=True)
    longitude = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    is_agreed = serializers.BooleanField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    user_type = serializers.CharField(required=True)
    document_no = serializers.IntegerField(required=True)


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


class SendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=50, required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ChangePasswordSerializer(serializers.Serializer):
    code = serializers.IntegerField(required=True)
    new_password = serializers.CharField(required=True)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class IndividualSerializer(serializers.ModelSerializer):

    class Meta:
        model = Individual
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company

        fields = '__all__'


class AddVerificationBadgeSerializer(serializers.Serializer):
    document_type = serializers.CharField(required=True)
    front_pic = serializers.ImageField(required=True)
    back_pic = serializers.ImageField(required=False)
    user_with_document_pic=serializers.ImageField(required=True)

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
    user_with_document_pic=serializers.ImageField(required=False)
    is_verified=serializers.BooleanField(required=True)




class UpdatePasswordSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UpdateAdressSerializer(serializers.Serializer):

    latitude = serializers.CharField(required=True)
    longitude = serializers.CharField(required=True)
    address = serializers.CharField(required=True)


class UpdateDOBSerializer(serializers.Serializer):
    birth_date = serializers.CharField(required=True)


class UpdateEmailSerializer(serializers.Serializer):
    email_address = serializers.CharField(required=True)


class UpdateDataSerializer(serializers.Serializer):

    user_with_document_pic = serializers.ImageField(required=True)
    full_name = serializers.CharField(required=True)
    document_type = serializers.CharField(required=True)
    document_no = serializers.IntegerField(required=True)

    def validate(self, data):
        """
        Check document_type is valid
        """
        if data['document_type'] not in ["passport", "id_card"]:
            raise serializers.ValidationError("document_type must be id_card or passport")
        return data


class UpdateCompanyNameAndRutSerializer(serializers.Serializer):
    company_name = serializers.CharField(required=True)
    rut = serializers.CharField(required=True)


class AddCompanyPicSerializer(serializers.Serializer):
    profile_pic = serializers.ImageField(required=True)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'