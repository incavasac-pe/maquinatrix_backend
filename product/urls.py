from django.urls import include, path

from product.products_views import *

app_name = 'product'
urlpatterns = [

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
    path('get-all-product-type/', GetAllProductTypes.as_view()),
    path('create-product-category/', CreateProductCategory.as_view()),
    path('get-all-categories/', GetAllProductCategories.as_view()),

]