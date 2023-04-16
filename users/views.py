from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import *
import random
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMessage
from maquinatrix_backend.settings import EMAIL_HOST_USER
import secrets

# Create your views here.
class Registration(APIView):
    permission_classes = (AllowAny,)

    def post( self,request):
        data = request.data
        if data['user_type'] == "company":
            serializer = AddCompanySerializer(data=data)
            if serializer.is_valid():
                if not User.objects.filter(email=serializer.validated_data['email']):
                    user_obj=User.objects.create_user(email=serializer.validated_data['email'].lower(),
                                                 username=serializer.validated_data['email'],is_staff=True)
                    user_obj.set_password(serializer.validated_data['password'])
                    user_obj.save()
                    user = authenticate(username=serializer.validated_data['email'].lower(),
                                        password=serializer.validated_data['password'])
                    token = Token.objects.get_or_create(user=user_obj)[0].key
                    company_obj = Company.objects.create(rut=serializer.validated_data['rut'],
                                                         company_name=serializer.validated_data['company_name'],
                                                         is_email_verified=serializer.validated_data['is_email_verified'],latitude=serializer.validated_data['latitude'],longitude=serializer.validated_data['longitude'],address=serializer.validated_data['address'],user=user_obj)

                    subject = "Email verification"
                    message1="maquinatrix"
                    context={'token': token}
                    message = render_to_string('verify_email.html',context)
                    email=data['email']
                                    # print("email==",email)
                    recipient_list=[email]
                    send_mail(subject, EMAIL_HOST_USER, message1, recipient_list,html_message=message,fail_silently=False)


                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(
                        {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Email Already Exists"})

            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        else:
            serializer = AddIndividualSerializer(data=data)
            if serializer.is_valid():
                # user_obj = User.objects.create(password=serializer.validated_data['password'],email=serializer.validated_data['email'].lower(),username=serializer.validated_data['email'])


                if not User.objects.filter(email=serializer.validated_data['email']):
                    user_obj = User.objects.create_user(email=serializer.validated_data['email'].lower(),
                                                        username=serializer.validated_data['email'])
                    user_obj.set_password(serializer.validated_data['password'])
                    user_obj.save()
                    user = authenticate(username=serializer.validated_data['email'].lower(),
                                        password=serializer.validated_data['password'])
                    token = Token.objects.get_or_create(user=user_obj)[0].key
                indivdual_obj=Individual.objects.create(id_document=serializer.validated_data['id_document'],
                                                        id_number=serializer.validated_data['id_number'],
                                                        birth_date=serializer.validated_data['birth_date'],
                                                        # birth_date=serializer.validated_data[' birth_date'],
                                                        first_name=serializer.validated_data['first_name'],
                                                        last_name=serializer.validated_data['last_name'],
                                                        latitude=serializer.validated_data['latitude'],
                                                        longitude=serializer.validated_data['longitude'],
                                                        address=serializer.validated_data['address'],user=user_obj)


                subject = "Email verification"
                message1 = "maquinatrix"
                context = {'token': token}
                message = render_to_string('verify_email.html', context)
                email = data['email']
                # print("email==",email)
                recipient_list = [email]
                send_mail(subject, EMAIL_HOST_USER, message1, recipient_list, html_message=message, fail_silently=False)

                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassLoginApi(APIView):
    permission_classes = (AllowAny,)
    serializer_class =  LoginSerializer


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        response = serializer.is_valid(raise_exception=True)
        return self.on_valid_request_data(serializer.validated_data, request)

    def on_valid_request_data(self, data, request):
        # username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user_obj = User.objects.filter(email=email).last()

        if user_obj:
            if user_obj.is_staff == True:
                obj = Company.objects.filter(user_id=user_obj.id).last()
            else:
                obj = Individual.objects.filter(user_id=user_obj.id).last()
            if obj.is_email_verified:

                user = authenticate(username=user_obj.email, password=password)
                if user is not None:
                    user_profile_serializer = UserSerializer(user)
                    user_profile_serializer = user_profile_serializer.data
                    token, created = Token.objects.get_or_create(user=user)
                    response = {
                        'token': token.key,
                        'user_profile': user_profile_serializer
                    }
                    return Response(
                        {"status_code": status.HTTP_200_OK, "success": True, "message": "user login success",
                         "data": response})

                else:
                    return Response(
                    {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message":"Credentials not valid"})

            else:
                return Response(
                    {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Please verify your email"})

        else:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "user login fail"})





class VerifyEmail(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user=request.user
        print(user)

        # if user. obj.values_list('is_staff') == True:

        if user.is_staff == True:
            print("user True")
            obj = Company.objects.filter(user_id=user.id).last()
            if obj.is_email_verified:
                print("link expire")
                return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "link expired"})
            else:
                Company.objects.filter(user_id=user.id).update(is_email_verified=True)
                # obj.update(is_email_verified=True)
            return Response(
                {"status_code": status.HTTP_200_OK, "success": True, "message": "email verified"})
        else:
            obj = Individual.objects.filter(user_id=user.id).last()
            if obj.is_email_verified == False:
                Individual.objects.filter(user_id=user.id).update(is_email_verified=True)
                return Response(
                    {"status_code": status.HTTP_200_OK, "success": False, "message": "email verified"})
            else:
                print("link expire")
                return Response(
                    {"status_code": status.HTTP_200_OK, "success": False, "message": "link expired"})


class Sendcode(APIView):
    def post(self, request):
        data = request.data
        serializer = SendCodeSerializer(data=data)

        if serializer.is_valid():
            if  User.objects.filter(email=serializer.validated_data['email']):
                print("email  found ")

                code = random.randint(1000, 9999)
                # code=7957

                print(code)

                code_obj = Resetcode.objects.filter(code=code)
                user = User.objects.filter(email=serializer.validated_data['email']).last()

                obj = Resetcode.objects.filter(user_id=user.id).last()
                rest_obj=Resetcode.objects.all()

                while True:
                    if Resetcode.objects.filter(code=code).exists():

                        code = random.randint(1000, 9999)


                    elif Resetcode.is_expired==True:
                        Resetcode.objects.filter(user_id=user.id).update(is_expired=False)


                    else:
                        break
                    # at least one object satisfying query exists



                user = User.objects.filter(email=serializer.validated_data['email']).last()
                reset=Resetcode.objects.filter(user_id=user.id).update(is_expired=True)


                # if code == Resetcode.code:
                #     code = random.randint(1000, 9999)
                #     code='1111'


                user = User.objects.filter(email=serializer.validated_data['email']).last()
                resetpassword_obj = Resetcode.objects.create(user_id=user.id, code=code)


                subject = "subject reset password code"
                message1 = "new message code is here"

                context = {'code': code}
                message = render_to_string('send_code.html', context)
                email = data['email']
                recipient_list = [email]
                send_mail(subject, EMAIL_HOST_USER, message1, recipient_list, html_message=message, fail_silently=False)
                return Response({
                    'code': code,
                    'data': serializer.data,
                    'message': "your four digit code is created"
                }, status=status.HTTP_200_OK)
            else:
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "link expired"}



        # users = User.objects.filter(email=user)
        # print(user)




