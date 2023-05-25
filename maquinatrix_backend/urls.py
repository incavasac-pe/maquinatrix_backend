"""maquinatrix_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from product.products_views import *
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Registration.as_view()),
    path('login/', ClassLoginApi.as_view()),
    path('verify-email/', VerifyEmail.as_view()),
    path('send-code/', SendCode.as_view()),
    path('change-password/', ChangePassword.as_view()),
    path('get-user/', GetUserdata.as_view()),
    path('verification-badge/', VerificationBadgeView.as_view()),
    path('update-password/', UpdatePasswordView.as_view()),
    path('update-dob/', UpdateIndividualDobView.as_view()),
    path('update-address/', UpdateAddressView.as_view()),
    path('update-email/', UpdateEmailView.as_view()),
    path('update-individual-info/', UpdateIndividualInfoView.as_view()),
    path('update-company-name-and-rut/', UpdateCompanyNameAndRutView.as_view()),
    path('update-company-pic/', UpdateCompanyPicView.as_view()),

    path('product/',include('product.urls'))

]
