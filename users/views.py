from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import *
import random
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import  render_to_string
from maquinatrix_backend.settings import EMAIL_HOST_USER


class Registration(APIView):
    permission_classes = (AllowAny,)

    def post( self,request):
        data = request.data
        if data['user_type'] not in ["company","individual"]:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False,"message": "user_type must be company or individual"})

        if data['user_type'] == "company":
            serializer = AddCompanySerializer(data=data)
            if serializer.is_valid():
                if not User.objects.filter(email=serializer.validated_data['email'].lower()):
                    user_obj=User.objects.create_user(email=serializer.validated_data['email'].lower(),username=serializer.validated_data['email'],is_staff=True)
                    user_obj.set_password(serializer.validated_data['password'])
                    user_obj.save()
                    token = Token.objects.get_or_create(user=user_obj)[0].key
                    Company.objects.create(rut=serializer.validated_data['rut'],
                                                         company_name=serializer.validated_data['company_name'],
                                                         latitude=serializer.validated_data['latitude'],longitude=serializer.validated_data['longitude'],address=serializer.validated_data['address'],user=user_obj)
                    subject = "Email verification"
                    message1="http://localhost:3000/registro_exitoso/{{token}}".format(token)
                    context={'token': token}
                    message = render_to_string('verify_email.html',context)
                    email=data['email']
                    print("html=========",message)
                    recipient_list=[email]
                    send_mail(subject, EMAIL_HOST_USER, message1, recipient_list,html_message=message,fail_silently=True)
                    return Response(
                        {"status_code": status.HTTP_201_CREATED, "success": True, "message": "company registered",
                         "data": serializer.data})
                else:
                    return Response(
                        {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Email Already Exists"})

            else:
                return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid Payload",
                 'errors': serializer.errors})

        else:
            serializer = AddIndividualSerializer(data=data)
            if serializer.is_valid():

                if not User.objects.filter(email=serializer.validated_data['email'].lower()):
                    user_obj = User.objects.create_user(email=serializer.validated_data['email'].lower(),
                                                        username=serializer.validated_data['email'])
                    user_obj.set_password(serializer.validated_data['password'])
                    user_obj.save()
                    token = Token.objects.get_or_create(user=user_obj)[0].key
                    Individual.objects.create(id_document=serializer.validated_data['id_document'],
                                                        id_number=serializer.validated_data['id_number'],
                                                        birth_date=serializer.validated_data['birth_date'],
                                                        first_name=serializer.validated_data['first_name'],
                                                        last_name=serializer.validated_data['last_name'],
                                                        latitude=serializer.validated_data['latitude'],
                                                        longitude=serializer.validated_data['longitude'],
                                                        address=serializer.validated_data['address'],
                                                        document_no=serializer.validated_data['document_no'],
                                                        user=user_obj)

                    subject = "Email verification"
                    message1 = "maquinatrix"
                    context = {'token': token}
                    message = render_to_string('verify_email.html', context)
                    email = data['email']

                    recipient_list = [email]
                    send_mail(subject, EMAIL_HOST_USER, message1, recipient_list, html_message=message, fail_silently=True)
                    return Response(
                        {"status_code": status.HTTP_201_CREATED, "success": True, "message": "individual registered",
                         "data": serializer.data})

                else:
                    return Response(
                        {"status_code": status.HTTP_400_BAD_REQUEST, "success": False,
                         "message": "Email Already Exists"})
            else:
                 return Response(
                 {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid Payload"
                                                                                           ,"errors":serializer.errors})


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
        user_id = request.user.id
        user=request.user
        token = Token.objects.get_or_create(user=user_id)[0].key
        Token.objects.filter(user_id=user_id)
        if UpdateEmail.objects.filter(token=token).exists():
            if user.is_staff == True:
                obj = Company.objects.filter(user_id=user.id).last()
                if obj.is_email_verified:
                    Company.objects.filter(user_id=user.id).update(is_email_verified=True)
                    update_email_obj = UpdateEmail.objects.get(token=token)
                    updated_email = update_email_obj.email_address
                    User.objects.filter(id=user_id).update(email=updated_email, username=updated_email)
                    UpdateEmail.objects.filter(token=token).delete()
                    return Response(
                    {"status_code": status.HTTP_200_OK, "success": True, "message": "email verified"})
                else:
                    return Response(
                        {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "link expired"})
            else:
                update_email_obj = UpdateEmail.objects.get(token=token)
                updated_email = update_email_obj.email_address

                User.objects.filter(id=user_id).update(email=updated_email, username=updated_email)
                UpdateEmail.objects.filter(token=token).delete()

                return Response(
                    {"status_code": status.HTTP_200_OK, "success": False, "message": "User updated"})

        else:
            if user.is_staff:
                obj = Company.objects.filter(user_id=user.id).last()
                if obj.is_email_verified:

                    return Response(
                        {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "link expired"})
                else:
                    Company.objects.filter(user_id=user.id).update(is_email_verified=True)
                return Response(
                    {"status_code": status.HTTP_200_OK, "success": True, "message": "email verified"})
            else:
                obj = Individual.objects.filter(user_id=user.id).last()
                if obj.is_email_verified:
                    return Response(
                        {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "link expired"})
                else:
                    Individual.objects.filter(user_id=user.id).update(is_email_verified=True)
                    return Response(
                        {"status_code": status.HTTP_200_OK, "success": True, "message": "email verified"})


class SendCode(APIView):
    def post(self, request):
        data = request.data
        serializer = SendCodeSerializer(data=data)

        if serializer.is_valid():
            if User.objects.filter(email=serializer.validated_data['email']):

                code = random.randint(1000, 9999)
                user = User.objects.filter(email=serializer.validated_data['email']).last()
                while True:
                    if Resetcode.objects.filter(code=code).filter(is_expired=False).exists():
                        code = random.randint(1000, 9999)
                    else:
                        break
                Resetcode.objects.filter(user_id=user.id).update(is_expired=True)
                Resetcode.objects.create(user_id=user.id, code=code)
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
                return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "link expired"}
                )
        else:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid payload",
                 'errors': serializer.errors}
            )


class ChangePassword(APIView):
    def post(self, request):
        data = request.data
        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            reset_obj = Resetcode.objects.filter(code=code)
            if reset_obj.exists() and not reset_obj.first().is_expired:
                user = reset_obj.first().user
                password = serializer.validated_data['password']
                user.set_password(password)
                user.save()
                reset_obj.first().is_expired = True
                reset_obj.first().save()
                return Response({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Reset code is invalid or expired.'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(
            {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid payload",
             'errors': serializer.errors})


class GetUserdata(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        if user.is_staff:
            instance = Company.objects.get(user_id=user)
            serializer = GetCompanyNameSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = Individual.objects.get(user_id=user)
            serializer = IndividualSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)


class VerificationBadgeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.user.id
        data = request.data
        serializer = AddVerificationBadgeSerializer(data=data)
        if serializer.is_valid():
            verification_obj = VerificationInfo.objects.create(document_type=serializer.validated_data['document_type'],
                                                               front_pic=serializer.validated_data['front_pic'],
                                                               user_with_document_pic=serializer.validated_data['user_with_document_pic'],
                                                               back_pic=serializer.validated_data.get('back_pic'),user_id=user_id)
            bagde_profile_serializer = VerificationBadgeResponseSerializer(verification_obj)
            badge_profile_serializer = bagde_profile_serializer.data
            response = {
                'badge_info': badge_profile_serializer
            }
            return Response(
                {"status_code": status.HTTP_201_CREATED, "success": True,
                 "data": response})

        else:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "invalid payload",
                 'errors': serializer.errors})


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    def post(self, request):
        self.object = self.get_object()
        serializer = self. serializer_class(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response( {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message":"incorect old password"})
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()

            return Response(
                {"status_code": status.HTTP_200_OK, "success": True, "message": "user password updated", })
        else:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid payload",
                 'errors': serializer.errors})

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


class UpdateAddressView(APIView):
    def put(self, request):
        user_id = request.user.id
        serializer = UpdateAdressSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            latitude = serializer.validated_data['latitude']
            longitude = serializer.validated_data['longitude']
            address = serializer.validated_data['address']
            if user.is_staff:
                Company.objects.filter(user_id=user_id).update(latitude=latitude, longitude=longitude, address=address)
                user_obj = Company.objects.get(user_id=user_id)
                response_serializer = CompanySerializer(user_obj)
            else:
                Individual.objects.filter(user_id=user_id).update(latitude=latitude,
                                                                  longitude=longitude, address=address)
                user_obj = Individual.objects.get(user_id=user_id)
                response_serializer = IndividualSerializer(user_obj)
            return Response(
                {"status_code": status.HTTP_200_OK, "success": True, "data": response_serializer.data})
        else:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid payload",
                 'errors': serializer.errors})


class UpdateIndividualDobView(APIView):
    def put(self, request):
        user_id = request.user.id
        serializer = UpdateDOBSerializer(data=request.data)
        if serializer.is_valid():

            birth_date = serializer.validated_data['birth_date']
            Individual.objects.filter(user_id=user_id).update(birth_date=birth_date)
            user_obj = Individual.objects.get(user_id=user_id)
            response_serializer = IndividualSerializer(user_obj)
            return Response(
                {"status_code": status.HTTP_200_OK, "success": True, "data": response_serializer.data})
        else:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid payload",
                 'errors': serializer.errors})


class UpdateEmailView(APIView):
    def post(self, request):
        data = request.data
        user_id = request.user.id
        serializer = UpdateEmailSerializer(data=data)
        if serializer.is_valid():
            if request.user.email == serializer.validated_data['email_address']:
                return Response(
                    {"status_code": status.HTTP_400_BAD_REQUEST, "success": False,
                     "message": "This is your current email"

                     }
                )
            else:
                token = Token.objects.get_or_create(user=user_id)[0].key
                if not User.objects.filter(email=serializer.validated_data['email_address']):
                    if UpdateEmail.objects.filter(token=token).exists():
                        UpdateEmail.objects.filter(token=token).delete()
                    email_address = serializer.validated_data['email_address']
                    UpdateEmail.objects.create(email_address=email_address, token=token)
                    subject = "Email verification"
                    message1 = "maquinatrix"
                    context = {'token': token}
                    message = render_to_string('verify_email.html', context)
                    recipient_list = [email_address]
                    send_mail(subject, EMAIL_HOST_USER, message1, recipient_list, html_message=message,
                                  fail_silently=False)

                    return Response(
                            {"status_code": status.HTTP_200_OK, "success": True,"message": "Check your email"})
                else:

                    return Response(
                        {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "User with this email"
                                                                                              " already exist"
                         }
                    )
        else:
            return Response(
                    {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid payload",
                     'errors': serializer.errors})


class UpdateIndividualInfoView(APIView):
    serializer_class = UpdateDataSerializer

    def put(self, request):
        user_id = request.user.id
        serializer = UpdateDataSerializer(data=request.data)
        if serializer.is_valid():
            profile_pic = serializer.validated_data['profile_pic']
            document_type = serializer.validated_data['document_type']
            document_no = serializer.validated_data['document_no']
            full_name = serializer.validated_data['full_name']
            full = full_name.split()
            Individual.objects.filter(user_id=user_id).update(profile_pic=profile_pic,id_document=document_type,
                                                              document_no=document_no,first_name=full[0],
                                                              last_name=full[1])
            individual_obj = Individual.objects.get(user_id=user_id)
            response_serializer = IndividualSerializer(individual_obj)
            return Response(
            {"status_code": status.HTTP_200_OK, "success": True,"data": response_serializer.data})
        else:
            return Response(
            {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid payload",
             'errors': serializer.errors})


class UpdateIndividualCompanyNameView(APIView):
    serializer_class = UpdateCompanyNameSerializer

    def put(self, request):
        user_id = request.user.id
        serializer = UpdateCompanyNameSerializer(data=request.data)
        if serializer.is_valid():

            company_name = serializer.validated_data['company_name']
            Company.objects.filter(user_id=user_id).update(company_name=company_name)
            instance = Company.objects.get(user_id=user_id)
            response_serializer = GetCompanyNameSerializer(instance)
            return Response(
            {"status_code": status.HTTP_200_OK, "success": True,"data": response_serializer.data})
        else:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "Invalid payload",
                 'errors': serializer.errors})



