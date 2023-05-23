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
from django.urls import path

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
    path('update-password/', ChangePasswordView.as_view()),
    path('update-dob/', UpdateIndividualDobView.as_view()),
    path('update-address/', UpdateAddressView.as_view()),
    path('update-email/', UpdateEmailView.as_view()),
    path('update-individual-info/', UpdateIndividualInfoView.as_view()),
    path('update-company-name-and-rut/', UpdateCompanyNameAndRutView.as_view()),
    path('update-company-pic/', UpdateCompanyPicView.as_view()),



    path('create-brand/', CreateBrand.as_view()),
    path('create-model/', CreateModel.as_view()),
    path('create-region/', CreateProductRegion.as_view()),
    path('get-all-brands/', GetAllBrands.as_view()),
    path('get-all-regions/', GetAllRegions.as_view()),
    path('create-label/', CreateProductLabel.as_view()),
    path('create-all-labels/', CreateAllProductLabel.as_view()),
    path('get-all-labels/', GetAllLabels.as_view()),
    path('get-all-product-types/', GetAllProductTypes.as_view()),
    path('get-machine-by-industry-id/', GetMachineTypesByIndustryId.as_view()),
    path('get-all-machine-types/', GetAllMachineTypes.as_view()),
    path('get-categories-by-product-type-id/', GetCategoriesByProductTypeId.as_view()),


    path('create-plan/', CreateProductPlan.as_view()),
    path('get-all-plans/', GetAllPlans.as_view()),
    path('create-all-plans/', CreateAllProductPlans.as_view()),

    path('create-industry/', CreateIndustry.as_view()),
    path('get-all-industries/', GetAllIndustries.as_view()),
    path('create-machine-type/', CreateMachineType.as_view()),


    path('create-city/', CreateProductCity.as_view()),
    path('get-all-cities/', GetAllCities.as_view()),

    path('create-year/', CreateProductYear.as_view()),
    path('get-all-years/', GetAllYears.as_view()),
    path('get-years-against-brand-and-model-id/', GetYearsAgainstModelIdAndBrandId.as_view()),

    path('get-cities-by-region/', GetCitiesByRegionid.as_view()),
    path('get-models-by-brand-id/', GetModelsAgainstBrandId.as_view()),
    path('create-product-images/', SaveProductImages.as_view()),
    path('get-all-models/', GetAllModels.as_view()),
    path('create-product/', CreateProduct.as_view()),
    path('create-product-condition/', CreateProductCondition.as_view()),
    path('create-product-type/', CreateProductType.as_view()),
    path('create-all-product-types/', CreateAllProductType.as_view()),
    path('get-all-product_type/', GetAllProductTypes.as_view()),
    path('create-product-category/', CreateProductCategory.as_view()),
    path('get-all-categories/', GetAllProductCategories.as_view()),

]
