from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from product.products_serializers import *
from rest_framework.response import Response
from maquinatrix_backend.services import *
from .models import *
from maquinatrix_backend import services
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, parsers


class CreateBrand(APIView):
    permission_classes = (IsAuthenticated,)

    def post( self,request):
        data = request.data

        serializer = CreateBrandSerializer(data=data)
        if serializer.is_valid():
            brand_obj = Brand.objects.create(name=serializer.validated_data['new_brand_name'].lower())
            response_serializer = BrandSerializer(brand_obj)
            return Response(
                services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                          msg='New brand added'), status=status.HTTP_201_CREATED)
        else:
            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="Invalid Payload", errors=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)


class CreateModel(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        data = request.data
        serializer = CreateModelSerializer(data=data)

        if serializer.is_valid():
            brand_id = serializer.validated_data['brand_id']
            model_name = serializer.validated_data['new_model_name']
            model_obj = Model.objects.create(name=model_name,
                                             brand_id=brand_id)
            response_serializer = ModelSerializer(model_obj)

            return Response(
                services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                          msg='New Model created'), status=status.HTTP_201_CREATED)
        else:
            return Response(
             services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                              msg="Invalid Payload", errors=serializer.errors),
             status=status.HTTP_400_BAD_REQUEST)


class CreateProductCondition(APIView):
    permission_classes = (IsAuthenticated,)

    def post( self,request):
        data = request.data

        serializer = CreateProductConditionSerializer(data=data)
        if serializer.is_valid():
            condition_obj = Condition.objects.create(product_condition=serializer.validated_data['product_condition'],
                                                     hours_used=serializer.validated_data['hours_used'],
                                                     km_run=serializer.validated_data['km_run'],)
            response_serializer = CreateProductConditionSerializer(condition_obj)
            return Response(
                services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                          msg='Condition  added'), status=status.HTTP_201_CREATED)
        else:
            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="Condition not created", errors=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)


class CreateProductRegion(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        serializer = CreateRegionSerializer(data=data)
        if serializer.is_valid():
            region_obj = Region.objects.create(name=serializer.validated_data['new_region_name'].lower())
            response_serializer = RegionSerializer(region_obj)
            return Response(
                services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                          msg='New region created'), status=status.HTTP_201_CREATED)
        else:
            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="Invalid Payload", errors=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)


class GetAllBrands(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        brand_objs = Brand.objects.all()
        response_serializer = BrandSerializer(brand_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                      msg='All Brands'), status=status.HTTP_200_OK)


class GetAllRegions(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        region_objs = Region.objects.all()
        response_serializer = RegionSerializer(region_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                      msg='All Regions'), status=status.HTTP_200_OK)


class GetAllMachineTypes(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        machine_objs = MachineType.objects.all()
        response_serializer = MachineSerializer(machine_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                      msg='All Machines'), status=status.HTTP_200_OK)


class CreateProductLabel(APIView):
    permission_classes = (IsAuthenticated,)

    def post( self,request):
        data = request.data

        serializer = CreateProductLabelSerializer(data=data)
        if serializer.is_valid():
            new_label = serializer.validated_data['new_label_name']
            label_price = serializer.validated_data['label_price']
            label_obj = Label.objects.create(name=new_label,
                                             price=label_price)
            response_serializer = LabelSerializer(label_obj)
            return Response(
                services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                          msg='New Label created'), status=status.HTTP_201_CREATED)
        else:
            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="Invalid payload", errors=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)


class CreateProductCity(APIView):
    permission_classes = (IsAuthenticated,)

    def post( self,request):
        data = request.data

        serializer = CreateProductCityandRegionSerializer(data=data)
        if serializer.is_valid():
            region_id = serializer.validated_data['region_id']
            city_name = serializer.validated_data['city_name'].lower()
            city_obj = City.objects.create(region_id=region_id, city_name=city_name)
            response_serializer = CitySerializer(city_obj)
            return Response(
                            services.success_response(status_code=status.HTTP_201_CREATED,
                                                      data=response_serializer.data,msg='New city Created'),
                                                      status=status.HTTP_201_CREATED)
        else:
             return Response(
                 services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                           msg="Invalid Payload", errors=serializer.errors),
                 status=status.HTTP_400_BAD_REQUEST)


class CreateProductPlan(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data

        serializer = CreateProductPlanSerializer(data=data)
        if serializer.is_valid():
            name = serializer.validated_data['new_plan_name'].lower()
            is_top_seller = serializer.validated_data['is_top_seller']
            price = serializer.validated_data['price']
            plan_obj = Plan.objects.create(name=name, price=price,is_top_seller=is_top_seller)
            response_serializer = ProductPlanSerializer(plan_obj)
            return Response(
                            services.success_response(status_code=status.HTTP_201_CREATED,
                                                      data=response_serializer.data,msg='New plan Created'),
                                                      status=status.HTTP_201_CREATED)
        else:
            return Response(
                 services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                           msg="Invalid Payload", errors=serializer.errors),
                 status=status.HTTP_400_BAD_REQUEST)


class CreateAllProductPlans(APIView):
        permission_classes = (IsAuthenticated,)

        def post(self, request):
            Plan.objects.all().delete()
            for plan in plan_types:
                i = 0
                Plan.objects.create(name=plan, price=plan_prices[i], is_top_seller=plan_seller[i])
                i += 1

            prod_plan = Plan.objects.all()
            response_serializer = ProductPlanSerializer(prod_plan, many=True)
            return Response(
                 services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                           msg='Product Plans created'),
                 status=status.HTTP_201_CREATED)


class CreateIndustry(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data

        serializer = CreateIndustrySerializer(data=data)
        if serializer.is_valid():
            name = serializer.validated_data['new_industry_name'].lower()

            industry_obj = Industry.objects.create(name=name)
            response_serializer = IndustrySerializer(industry_obj)
            return Response(
                services.success_response(status_code=status.HTTP_201_CREATED,
                                          data=response_serializer.data,msg='New industry Created'),
                status=status.HTTP_201_CREATED)
        else:
             return Response(
                 services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                           msg="Invalid Payload", errors=serializer.errors),
                 status=status.HTTP_400_BAD_REQUEST)


class CreateMachineType(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data

        serializer = CreateMachineTypeSerializer(data=data)
        if serializer.is_valid():
            machine_name = serializer.validated_data['machine_name'].lower()
            industry_id = serializer.validated_data['industry_id']

            machine_obj = MachineType.objects.create(name=machine_name,industry_id=industry_id)
            response_serializer = MachineSerializer(machine_obj)
            return Response(
                            services.success_response(status_code=status.HTTP_201_CREATED,
                                                      data=response_serializer.data,msg='New machine Created'),
                                                      status=status.HTTP_201_CREATED)
        else:
            return Response(
                 services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                           msg="Invalid Payload", errors=serializer.errors),
                 status=status.HTTP_400_BAD_REQUEST)


class GetAllCities(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        city_objs = City.objects.all()
        response_serializer = CitySerializer(city_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,msg='All Cities'),
            status=status.HTTP_200_OK)


class GetAllYears(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        year_objs = Year.objects.all()
        response_serializer = YearSerializer(year_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,msg='All Years'),
            status=status.HTTP_200_OK)


class CreateProductYear(APIView):
    permission_classes = (IsAuthenticated,)

    def post( self,request):
        data = request.data

        serializer = CreateYearSerializer(data=data)
        if serializer.is_valid():
            model_id = serializer.validated_data['model_id']
            brand_id = serializer.validated_data['brand_id']
            year_name = serializer.validated_data['new_year_name']

            year_obj = Year.objects.create(brand_id=brand_id, model_id=model_id, year=year_name)
            response_serializer = YearSerializer(year_obj)
            return Response(
                    services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                              msg='New Year created'), status=status.HTTP_201_CREATED)
        else:
            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="Invalid Payload", errors=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)


class GetAllLabels(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        label_objs = Label.objects.all()
        response_serializer = LabelSerializer(label_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK,data=response_serializer.data,
                                      msg='All Labels '), status=status.HTTP_200_OK)


class GetAllProductTypes(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        product_objs = ProductType.objects.all()
        response_serializer = ProducTypeSerializer(product_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK,data=response_serializer.data,
                                      msg='All Product types are'), status=status.HTTP_200_OK)


class GetMachineTypesByIndustryId(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = request.data
        serializer = GetMachineTypesSerializer(data=data)
        if serializer.is_valid():
            industry_id = serializer.validated_data['industry_id']
            machine_objs = MachineType.objects.filter(industry_id=industry_id)
            response_serializer = MachineSerializer(machine_objs, many=True)
            return Response(
                services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                          msg='All Machine types against this industry id'),
                status=status.HTTP_200_OK)
        else:
            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="Invalid Payload", errors=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)


class GetCategoriesByProductTypeId(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = request.data
        serializer = CreateProductCategoriesSerializer(data=data)
        if serializer.is_valid():
            product_type_id = serializer.validated_data['product_type_id']
            cat_objs = ProductCategories.objects.filter(product_type_id=product_type_id)
            response_serializer = ProductCategoriesSerializer(cat_objs, many=True)
            return Response(
                services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                          msg='All Product types categories against this  product type id'),
                status=status.HTTP_200_OK)
        else:
            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="Invalid Payload", errors=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)


class GetAllPlans(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        plan_objs = Plan.objects.all()
        response_serializer = PlanSerializer(plan_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK,data=response_serializer.data,
                                      msg='All Plans '), status=status.HTTP_200_OK)


class GetAllIndustries(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        industry_objs = Industry.objects.all()
        response_serializer = IndustrySerializer(industry_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK,data=response_serializer.data,
                                      msg='All Industries '), status=status.HTTP_201_CREATED)


class GetCitiesByRegionid(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        data = request.data
        serializer = AddCitySerializer(data=data)
        if serializer.is_valid():
            region_id = serializer.validated_data['region_id']
            city_objs = City.objects.filter(region_id=region_id)
            response_serializer = CitySerializer(city_objs, many=True)

            return Response(
                services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                          msg='All Cities Against this region id '), status=status.HTTP_201_CREATED)
        return Response(
            services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                      msg="Invalid Payload", errors=serializer.errors),
            status=status.HTTP_400_BAD_REQUEST)


class GetModelsAgainstBrandId(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = request.query_params
        payload_serializer = BrandIdSerializer(data=data)
        if payload_serializer.is_valid():
            brand_id = payload_serializer.validated_data['brand_id']
            model_objs = Model.objects.filter(brand_id=brand_id)
            response_serializer = ModelSerializer(model_objs, many=True)
            return Response(
                services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                          msg='All models against this brand id'), status=status.HTTP_200_OK)
        else:
            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,errors=payload_serializer.errors,
                                          msg="Invalid Payload"),
                status=status.HTTP_400_BAD_REQUEST)


class GetAllModels(APIView,):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        model_objs = Model.objects.all()
        response_serializer = ModelSerializer(model_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                      msg='All Models'), status=status.HTTP_200_OK)


class GetYearsAgainstModelIdAndBrandId(APIView,):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = request.query_params
        payload_serializer = Yearserializer(data=data)
        if payload_serializer.is_valid():

            year_objs = Year.objects.filter(model_id=data['model_id'], brand_id=data['brand_id'])

            response_serializer = YearSerializer(year_objs, many=True)
            return Response(
                services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                          msg='All years against model id and brand id are'), status=status.HTTP_200_OK)
        else:

            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="Invalid Payload", errors=payload_serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)


class SaveProductImages(APIView):

    def get(self, request):
        all_images = ProductImages.objects.all()
        serializer = ProductImagesSerializer(all_images, many=True)
        return Response(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = ProductImagesSerializer(data=data)
        product_id = request.data['product_id']

        # converts querydict to original dict
        product_pic = dict((request.data).lists())['product_pic']
        flag = 1
        arr = []
        for img_name in product_pic:
            modified_data = modify_input_for_multiple_files(product_id,img_name)
            file_serializer = ProductImagesSerializer(data=modified_data)

            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                return Response(
                    services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                              msg="Invalid Payload", errors=serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST)
                flag = 0
        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(
                services.failure_response(arr,status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="product_type with this name already exists.", errors=serializer.errors),
                status= status.HTTP_400_BAD_REQUEST)


class CreateProduct(APIView):
    # permission_classes = (IsAuthenticated,)

    def post( self,request):
        data = request.data
        serializer = NewProductSerializer(data=data)
        if serializer.is_valid():
            product_pics = serializer.validated_data.get('product_pics')
            brand_id = serializer.validated_data.get('brand_id')
            model_id = serializer.validated_data.get('model_id')
            year_id = serializer.validated_data.get('year_id')
            patent = serializer.validated_data.get('patent')
            product_type_id=serializer.validated_data.get('product_type_id')
            engine_no = serializer.validated_data.get('engine_no')
            chassis_no = serializer.validated_data.get('chassis_no')
            net_weight = serializer.validated_data.get('net_weight')
            power = serializer.validated_data.get('power')
            displacement = serializer.validated_data.get('displacement')
            torque = serializer.validated_data.get('torque')
            mixed_consumption = serializer.validated_data.get('mixed_consumption')
            transmission = serializer.validated_data.get('transmission')
            fuel = serializer.validated_data.get('fuel')
            traction = serializer.validated_data.get('traction')
            scheduled_maintenance = serializer.validated_data.get('scheduled_maintenance')
            technical_visit_included = serializer.validated_data.get('technical_visit_included')
            supply_included = serializer.validated_data.get('supply_included')
            product_condition = serializer.validated_data.get('product_condition')
            product_hours = serializer.validated_data.get('product_hours')
            product_km = serializer.validated_data.get('product_km')
            has_certificate = serializer.validated_data.get('has_certificate')
            has_insurance = serializer.validated_data.get('has_insurance')
            description = serializer.validated_data.get('description')
            insurance_doc = serializer.validated_data.get('insurance_doc')
            certificate_date = serializer.validated_data.get('certificate_date')
            certificate_doc = serializer.validated_data.get('certificate_doc')
            hourly_rate = serializer.validated_data.get('hourly_rate')
            minimum_hours = serializer.validated_data.get('minimum_hours')
            detailed = serializer.validated_data.get('detailed')
            dispatch_included = serializer.validated_data.get('dispatch_included')
            operator_included = serializer.validated_data.get('operator_included')
            maq_lease_contract = serializer.validated_data.get('maq_lease_contract')
            lease_guaranteed_condition_checklist = serializer.validated_data.get('lease_guaranteed_condition_checklist')
            percentage_amount = serializer.validated_data.get('percentage_amount')
            percentage = serializer.validated_data.get('percentage')
            title = serializer.validated_data.get('title')
            plan_id = serializer.validated_data['product_plan_id']
            category_type_id = serializer.validated_data['product_category_id']
            industry_id = serializer.validated_data['industry_id']
            machine_type_id = serializer.validated_data['machine_type_id']
            city_id = serializer.validated_data['city_id']
            region_id = serializer.validated_data['region_id']

            product_type_obj = ProductType.objects.filter(id=product_type_id)
            if product_type_obj:
                product_id_obj = product_type_obj[0].id
                product_name_obj = product_type_obj[0].name
            else:
                return Response(
                    services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                              msg="product_id does not present", ),
                    status=status.HTTP_400_BAD_REQUEST)

            category_type_obj = ProductCategories.objects.filter(id=category_type_id)
            if category_type_obj:
                category_id_obj = category_type_obj[0].id
                category_name_obj = category_type_obj[0].name
            else:
                return Response(
                    services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,errors=serializer.errors,
                                              msg="category_id does not present", ),
                    status=status.HTTP_400_BAD_REQUEST)

            if product_name_obj == "rent" and category_name_obj == "machine and vehicles":
                label_id = serializer.validated_data['product_label_id']
                label_obj = Label.objects.filter(id=label_id).last()
                if not label_obj:
                    return Response(
                        services.failure_response(status_code=status.HTTP_400_BAD_REQUEST, errors=serializer.errors,
                                                  msg="no label against this id", ),
                        status=status.HTTP_400_BAD_REQUEST)
                if region_id:
                    product_obj = Product.objects.create(product_type_id=product_id_obj,
                                                         product_category_id=category_id_obj,
                                                         product_pics=product_pics,
                                                         brand_id=brand_id,
                                                         model_id=model_id,
                                                         year_id=year_id,
                                                         patent=patent,
                                                         engine_no=engine_no,
                                                         chassis_no=chassis_no,
                                                         net_weight=net_weight,
                                                         power=power,
                                                         displacement=displacement,
                                                         torque=torque,
                                                         mixed_consumption=mixed_consumption,
                                                         transmission=transmission,
                                                         fuel=fuel,
                                                         traction=traction,
                                                         scheduled_maintenance=scheduled_maintenance,
                                                         technical_visit_included=technical_visit_included,
                                                         supply_included=supply_included,
                                                         product_condition=product_condition,
                                                         has_certificate=has_certificate,
                                                         region_id=region_id,
                                                         has_insurance=has_insurance,
                                                         city_id=city_id,
                                                         description=description,
                                                         product_label=label_obj,
                                                         plan_id=plan_id,
                                                         title=title,
                                                         industry_id=industry_id,
                                                         machine_type_id=machine_type_id)
                    product_id=product_obj.id
                    if product_condition == "used":
                        Condition.objects.create(product_condition=product_condition,
                                                 hours_used=product_hours,
                                                 km_run=product_km)
                    if has_insurance:
                        Insurance.objects.create(file=insurance_doc,product_id=product_id)
                    if has_certificate:
                        Certificate.objects.create(date=certificate_date,file=certificate_doc,product_id=product_id)
                    if product_name_obj == "rent":
                        RentInfo.objects.create(product_id=product_id,
                                                hourly_rate=hourly_rate,
                                                minimum_hours =minimum_hours,
                                                detailed =detailed,
                                                dispatch_included =dispatch_included,
                                                operator_included =operator_included,
                                                maq_lease_contract =maq_lease_contract,
                                                lease_guaranteed_condition_checklist=lease_guaranteed_condition_checklist,
                                                percentage_amount =percentage_amount,
                                                percentage =percentage,
                                                )
                    product_pics = dict((request.data).lists())['product_pics']
                    for img_name in product_pics:
                            modified_data = modify_input_for_multiple_files(product_id, img_name)
                            file_serializer = ProductImagesSerializer(data=modified_data)
                            if file_serializer.is_valid():
                                product_id = file_serializer.validated_data.get('product_id')
                                product_pics = file_serializer.validated_data.get('product_pics')
                                ProductImages.objects.create(product_id=product_id,
                                                             product_pics=product_pics)
                            else:
                                return Response(
                                    services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                                              errors=serializer.errors,
                                                              msg="region_id  does not present", ),
                                    status=status.HTTP_400_BAD_REQUEST)
                    response_serializer = ProductSerializer(product_obj)
                    return Response(
                        services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                                  msg='Product  added'), status=status.HTTP_201_CREATED, )
            else:
                if product_name_obj == "rent" and category_name_obj == "equipments and tools":
                    region_id = serializer.validated_data['region_id']
                    region_id_exists = Region.objects.filter(id=region_id).exists()
                    city_id = serializer.validated_data['city_id']
                    city_id_obj = Region.objects.filter(id=city_id).exists()
                    label_id = serializer.validated_data['product_label_id']
                    label_obj = Label.objects.filter(id=label_id).last()
                    if not label_obj:
                        return Response(
                            services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                                      msg="no label against this label_id", errors=serializer.errors),
                            status=status.HTTP_400_BAD_REQUEST)
                    if region_id_exists:
                        product_pics = serializer.validated_data.get('product_pics')
                        brand_id = serializer.validated_data.get('brand_id')
                        model_id = serializer.validated_data.get('model_id')
                        year_id = serializer.validated_data.get('year_id')
                        net_weight = serializer.validated_data.get('net_weight')
                        power = serializer.validated_data.get('power')
                        displacement = serializer.validated_data.get('displacement')
                        torque = serializer.validated_data.get('torque')
                        mixed_consumption = serializer.validated_data.get('mixed_consumption')
                        transmission = serializer.validated_data.get('transmission')
                        fuel = serializer.validated_data.get('fuel')
                        traction = serializer.validated_data.get('traction')
                        scheduled_maintenance = serializer.validated_data.get('scheduled_maintenance')
                        technical_visit_included = serializer.validated_data.get('technical_visit_included')
                        supply_included = serializer.validated_data.get('supply_included')
                        product_condition = serializer.validated_data.get('product_condition')
                        product_hours = serializer.validated_data.get('product_hours')
                        product_km = serializer.validated_data.get('product_km')
                        has_certificate = serializer.validated_data.get('has_certificate')
                        region = serializer.validated_data.get('region_id')
                        has_insurance = serializer.validated_data.get('has_insurance')
                        city = serializer.validated_data.get('city_id')
                        description = serializer.validated_data.get('description')
                        insurance_doc=serializer.validated_data.get('insurance_doc')
                        certificate_date = serializer.validated_data.get('certificate_date')
                        certificate_doc = serializer.validated_data.get('certificate_doc')
                        hourly_rate = serializer.validated_data.get('hourly_rate')
                        minimum_hours = serializer.validated_data.get('minimum_hours')
                        detailed = serializer.validated_data.get('detailed')
                        dispatch_included = serializer.validated_data.get('dispatch_included')
                        operator_included = serializer.validated_data.get('operator_included')
                        maq_lease_contract = serializer.validated_data.get('maq_lease_contract')
                        lease_guaranteed_condition_checklist = serializer.validated_data.get('lease_guaranteed_condition_checklist')
                        percentage_amount = serializer.validated_data.get('percentage_amount')
                        percentage = serializer.validated_data.get('percentage')
                        title = serializer.validated_data.get('title')
                        product_obj = Product.objects.create(product_type_id=product_id_obj,
                                                             product_category_id=category_id_obj,
                                                             product_pics=product_pics,
                                                             brand_id=brand_id,
                                                             model_id=model_id,
                                                             year_id=year_id,
                                                             net_weight=net_weight,
                                                             power=power,
                                                             displacement=displacement,
                                                             torque=torque,
                                                             mixed_consumption=mixed_consumption,
                                                             transmission=transmission,
                                                             fuel=fuel,
                                                             traction=traction,
                                                             scheduled_maintenance=scheduled_maintenance,
                                                             technical_visit_included=technical_visit_included,
                                                             supply_included=supply_included,
                                                             product_condition=product_condition,
                                                             has_certificate=has_certificate,
                                                             region_id=region,
                                                             has_insurance=has_insurance,
                                                             city_id=city,
                                                             description=description,
                                                             product_label=label_obj,
                                                             plan_id=plan_id,
                                                             title=title,
                                                             industry_id=industry_id,
                                                             machine_type_id=machine_type_id)
                        product_id=product_obj.id
                        if product_condition == "used":
                            Condition.objects.create(product_condition=product_condition,
                                                     hours_used=product_hours,
                                                     km_run=product_km)
                        if has_insurance:
                            Insurance.objects.create(file=insurance_doc,product_id=product_id)
                        if has_certificate:
                            Certificate.objects.create(date=certificate_date,file=certificate_doc,product_id=product_id)
                        if product_name_obj == "rent":
                            RentInfo.objects.create(product_id=product_id,
                                                    hourly_rate=hourly_rate,
                                                    minimum_hours =minimum_hours,
                                                    detailed =detailed,
                                                    dispatch_included =dispatch_included,
                                                    operator_included =operator_included,
                                                    maq_lease_contract =maq_lease_contract,
                                                    lease_guaranteed_condition_checklist=lease_guaranteed_condition_checklist,
                                                    percentage_amount =percentage_amount,
                                                    percentage =percentage,
                                                    )
                        product_pics = dict((request.data).lists())['product_pics']
                        for img_name in product_pics:
                                modified_data = modify_input_for_multiple_files(product_id, img_name)
                                file_serializer = ProductImagesSerializer(data=modified_data)
                                if file_serializer.is_valid():
                                    product_id = file_serializer.validated_data.get('product_id')
                                    product_pics = file_serializer.validated_data.get('product_pics')
                                    ProductImages.objects.create(product_id=product_id,
                                                                 product_pics=product_pics)
                                else:
                                    return Response(
                                        services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                                                  msg="Invalid Payload", errors=serializer.errors),
                                        status=status.HTTP_400_BAD_REQUEST)
                        response_serializer = ProductSerializer(product_obj)
                        return Response(
                            services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                                      msg='Product added'),
                            status=status.HTTP_201_CREATED, )
        else:
            return Response(
                services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                          msg="Product  not added", errors=serializer.errors),
                status=status.HTTP_400_BAD_REQUEST)


class CreateProductType(APIView):
        permission_classes = (IsAuthenticated,)

        def post(self, request):
            data = request.data
            serializer = CreateProductTypeSerializer(data=data)
            if serializer.is_valid():
                name = serializer.validated_data['product_type'].lower()
                type_obj = ProductType.objects.create(
                    name=name)
                response_serializer = ProductTypeSerializer(type_obj)
                return Response(
                    services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                                  msg='Product Type added'), status=status.HTTP_201_CREATED)
            else:
                return Response(
                    services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                              msg="Product Type not added", errors=serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST)


class GetAllProducTtypes(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        type_objs = ProductType.objects.all()
        response_serializer = ProducTypeSerializer(type_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK, data=response_serializer.data,
                                      msg='All Product types'), status=status.HTTP_200_OK, )


class CreateProductCategory(APIView):
        permission_classes = (IsAuthenticated,)

        def post(self, request):
            rent_obj = ProductType.objects.filter(name="rent")
            sale_obj = ProductType.objects.filter(name="sale")
            if not rent_obj:
                return Response(
                    services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                              msg="Rent not present in product type"),
                    status=status.HTTP_400_BAD_REQUEST)
            if not sale_obj:
                return Response(
                    services.failure_response(status_code=status.HTTP_400_BAD_REQUEST,
                                              msg="Sale not present in product type"),
                    status=status.HTTP_400_BAD_REQUEST)

            rent_id = rent_obj[0].id
            sale_id = sale_obj[0].id
            ProductCategories.objects.all().delete()
            for category in sale_catogories:
                ProductCategories.objects.create(product_type_id=sale_id, name=category)

            for category in rent_categories:
                ProductCategories.objects.create(product_type_id=rent_id, name=category)

            queryset = ProductCategories.objects.all()
            response_serializer = CategorySerializer(queryset, many=True)
            return Response(
                    services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                              msg='Product categories created'),
                    status=status.HTTP_201_CREATED, )


class GetAllProductCategories(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        cat_objs = ProductCategories.objects.all()
        serializer = CategoryTypeSerializer(cat_objs, many=True)
        return Response(
            services.success_response(status_code=status.HTTP_200_OK, data=serializer.data,
                                      msg='All Categories are'), status=status.HTTP_200_OK)


class CreateAllProductType(APIView):
        permission_classes = (IsAuthenticated,)

        def post(self, request):
            ProductType.objects.all().delete()
            for prod in product_types:
                ProductType.objects.create(name=prod)

            prod_type = ProductType.objects.all()
            response_serializer = ProductTypeSerializer(prod_type, many=True)

            return Response(
                services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                          msg='Product types created'),
                status=status.HTTP_201_CREATED, )


class CreateAllProductLabel(APIView):
        permission_classes = (IsAuthenticated,)

        def post(self, request):
            Label.objects.all().delete()

            i = 0
            for label in label_types:
                Label.objects.create(name=label, price=label_price[i])
                i += 1

            prod_label = Label.objects.all()
            response_serializer = LabelSerializer(prod_label, many=True)

            return Response(
                services.success_response(status_code=status.HTTP_201_CREATED, data=response_serializer.data,
                                          msg='Product labels created'),
                status=status.HTTP_201_CREATED)
