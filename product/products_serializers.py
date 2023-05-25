from .models import *
from rest_framework import serializers


class CreateBrandSerializer(serializers.Serializer):
    new_brand_name = serializers.CharField(required=True)
    def validate(self, data):
        """
        Check new_brand_name is valid
        """

        brand_id_exists = Brand.objects.filter(name=data['new_brand_name'].lower()).exists()
        if brand_id_exists:
            raise serializers.ValidationError("Brand with this name already exists")
        return data


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class ProductPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'


class ProductCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'


class IndustrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Industry
        fields = '__all__'


class MachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = MachineType
        fields = '__all__'


class ProductCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = '__all__'


class CreateProductCategoriesSerializer(serializers.Serializer):
        product_type_id = serializers.IntegerField(required=True)

        def validate(self, data):
            """
            Check product_type_id is valid
            """

            product_type_id_exists = ProductType.objects.filter(id=data['product_type_id']).exists()
            if not product_type_id_exists:
                raise serializers.ValidationError("Product type of this id does not exists")
            return data


class BrandIdSerializer(serializers.Serializer):
    brand_id = serializers.IntegerField(required=True)

    def validate(self, data):
        brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
        if not brand_id_exists:
            raise serializers.ValidationError("Brand id not present")
        return data


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = '__all__'


class AddCitySerializer(serializers.Serializer):
    region_id = serializers.IntegerField(required=True)

    def validate(self, data):
        region_id_exists = Region.objects.filter(id=data['region_id']).exists()
        if not region_id_exists:
            raise serializers.ValidationError("Region id not present")
        return data


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Year
        fields = '__all__'


class Yearserializer(serializers.Serializer):
    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.IntegerField(required=True)

    def validate(self, data):

        brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
        if not brand_id_exists:
            raise serializers.ValidationError("Brand id not present")

        model_id_exists = Model.objects.filter(id=data['model_id']).exists()
        if not model_id_exists:
            raise serializers.ValidationError("Model id not present")

        model_name_exists = Model.objects.filter(id=data['model_id'], brand_id=data['brand_id']).exists()
        if not model_name_exists:
            raise serializers.ValidationError("Model id against this brand id not present")

        return data


class getYearSerializer(serializers.Serializer):

    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.CharField(required=True)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'


class CreateModelSerializer(serializers.Serializer):
    brand_id = serializers.IntegerField(required=True)
    new_model_name = serializers.CharField(required=True)

    def validate(self, data):
        """
        Check params are valid
        """

        brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
        if not brand_id_exists:
            raise serializers.ValidationError("Brand id not present")

        model_name_exists=Model.objects.filter(name=data['new_model_name'],brand_id=data['brand_id']).exists()
        if model_name_exists:
            raise serializers.ValidationError("Model name with this brand id already exists")

        return data


class CreateYearSerializer(serializers.Serializer):
    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.IntegerField(required=True)
    new_year_name = serializers.IntegerField(required=True)

    def validate(self, data):

        brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
        if not brand_id_exists:
            raise serializers.ValidationError("Brand id not present")

        model_id_exists = Model.objects.filter(id=data['model_id'], brand_id=data['brand_id']).exists()
        if not model_id_exists:
            raise serializers.ValidationError("Model id with this brand id not exists")

        year_name_exists = Year.objects.filter(model_id=data['model_id'], brand_id=data['brand_id'],
                                               year=data['new_year_name']).exists()
        if year_name_exists:
            raise serializers.ValidationError("Year name with this brand id and model_id already exists")
        return data


class ProducTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'


class CategoryTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = '__all__'


class CreateProductConditionSerializer(serializers.Serializer):
    product_condition = serializers.CharField(required=True)
    hours_used = serializers.CharField(required=True)
    km_run = serializers.CharField(required=True)

    def validate(self, data):
        """
        Check product_condition is valid
        """
        if data['product_condition'] not in ["new", "used"]:
            raise serializers.ValidationError("product_condition must be new or used")
        return data


class CreateRegionSerializer(serializers.Serializer):
    new_region_name = serializers.CharField(required=True)

    def validate(self, data):
        region_name_exists = Region.objects.filter(name=data['new_region_name'].lower()).exists()
        if region_name_exists:
            raise serializers.ValidationError("Region with this name already exists")
        return data


class CreateProductLabelSerializer(serializers.Serializer):
    new_label_name = serializers.CharField(required=True)
    label_price = serializers.IntegerField(required=True)

    def validate(self, data):
            """
            Check new_label_name is valid
            """

            label_name_exists = Label.objects.filter(name=data['new_label_name']).exists()
            if label_name_exists:
                raise serializers.ValidationError(
                    "Label already exists")
            else:
                if data['new_label_name'] not in ["opportunity","offer","new","pre-owned","liquidation"]:
                    raise serializers.ValidationError("New label name can only be opportunity, "
                                                      "offer,new,liquidation, or pre-owned")
            return data


class CreateProductCitySerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    city = serializers.CharField(required=True)


class CreateProductCityandRegionSerializer(serializers.Serializer):

    region_id = serializers.IntegerField(required=True)
    city_name = serializers.CharField(required=True)

    def validate(self, data):

        region_id_exists = Region.objects.filter(id=data['region_id']).exists()
        if not region_id_exists:
            raise serializers.ValidationError("Region id not present")

        city_exists = City.objects.filter(city_name=data['city_name'],region_id=data['region_id']).exists()
        if city_exists:
            raise serializers.ValidationError("This city already exists in this region ")
        return data


class CreateProductRentSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    new_label_name = serializers.CharField(required=True)
    new_price = serializers.IntegerField(required=True)


class NewProductSerializer(serializers.Serializer):
    product_type_id = serializers.CharField(required=True)
    product_pics = serializers.ImageField(required=True)
    brand_id = serializers.IntegerField(required=False)
    model_id = serializers.IntegerField(required=False)
    year_id = serializers.IntegerField(required=True)
    patent = serializers.ImageField(required=True)
    engine_no = serializers.CharField(required=True)
    chassis_no = serializers.CharField(required=True)
    net_weight = serializers.FloatField(required=True)
    power = serializers.FloatField(required=True)
    displacement = serializers.FloatField(required=True)
    torque = serializers.FloatField(required=True)
    mixed_consumption = serializers.CharField(required=True)
    transmission = serializers.CharField(required=True)
    fuel = serializers.CharField(required=True)
    traction = serializers.CharField(required=True)
    scheduled_maintenance = serializers.BooleanField(required=True)
    technical_visit_included = serializers.BooleanField(required=True)
    supply_included = serializers.BooleanField(required=True)
    product_condition = serializers.CharField(required=True)
    product_hours = serializers.IntegerField(required=False,)
    product_km = serializers.CharField(required=False,)
    has_certificate = serializers.BooleanField(required=True)
    has_insurance = serializers.BooleanField(required=True)
    region_id = serializers.CharField(required=True)
    city_id = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    product_label_id = serializers.IntegerField(required=True)
    certificate_date = serializers.DateField(required=True)
    insurance_doc = serializers.ImageField(required=False)
    certificate_doc = serializers.ImageField(required=False)

    hourly_rate = serializers.IntegerField(required=True)
    minimum_hours = serializers.IntegerField(required=True)
    detailed = serializers.CharField(required=True)
    dispatch_included = serializers.CharField(required=True)
    operator_included = serializers.CharField(required=True)
    maq_lease_contract = serializers.CharField(required=True)
    lease_guaranteed_condition_checklist = serializers.CharField(required=True)
    percentage_amount = serializers.IntegerField(required=True)
    percentage = serializers.IntegerField(required=True)
    product_plan_id = serializers.CharField(required=True)
    title = serializers.CharField(required=False)
    product_category_id=serializers.CharField(required=True)
    industry_id=serializers.IntegerField(required=False)
    machine_type_id=serializers.IntegerField(required=False)


    def validate(self, data):

        if data['fuel'] not in ["diesel", "benzine", "not classified"]:
            raise serializers.ValidationError("fuel must be diesel, benzine or not classified")

        if data['product_condition'] not in ["new", "used"]:
            raise serializers.ValidationError("product_condition must be new or used")

        if data['transmission'] not in ["manual", "automatic","not classified"]:
            raise serializers.ValidationError("transmission must be manual, automatic or not classified")

        if data["brand_id"]:
            brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
            if not brand_id_exists:
                raise serializers.ValidationError("Brand id not present")

        year_id_exists = Year.objects.filter(id=data['year_id']).exists()
        if not year_id_exists:
            raise serializers.ValidationError("Year id not present")

        model_id_exists = Model.objects.filter(id=data['model_id']).exists()
        if not model_id_exists:
            raise serializers.ValidationError("model id not present")

        region_id_exists = Region.objects.filter(id=data['region_id']).exists()
        if not region_id_exists:
            raise serializers.ValidationError("region id not present")

        city_id_exists = City.objects.filter(id=data['city_id']).exists()
        if not city_id_exists:
            raise serializers.ValidationError("city id not present")

        industry_id_exists = Industry.objects.filter(id=data['industry_id']).exists()
        if not industry_id_exists:
            raise serializers.ValidationError("industry id not present")

        machine_type_id_exists = MachineType.objects.filter(id=data['machine_type_id']).exists()
        if not machine_type_id_exists:
            raise serializers.ValidationError("machine type id not present")

        product_cat_id_exists = ProductCategories.objects.filter(id=data['product_category_id']).exists()
        if not product_cat_id_exists:
            raise serializers.ValidationError("product category id not present")

        product_plan_id_exists = Plan.objects.filter(id=data['product_plan_id']).exists()
        if not product_plan_id_exists:
            raise serializers.ValidationError("product plan id not present")

        product_label_id_exists = Label.objects.filter(id=data['product_label_id']).exists()
        if not product_label_id_exists:
            raise serializers.ValidationError("label id not present")

        product_type_id_exists = ProductType.objects.filter(id=data['product_type_id']).exists()
        if not product_type_id_exists:
            raise serializers.ValidationError("product_type id not present")

        return data


class ProductImagesSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    product_pics = serializers.FileField()


class CreateProductTypeSerializer(serializers.Serializer):
    product_type = serializers.CharField(required=True)

    def validate(self, data):
        """
        Check product_type is valid
        """
        if data['product_type'] not in ["rent", "sale"]:
            raise serializers.ValidationError("Product type can only be rent or sale")
        product_exists = ProductType.objects.filter(name=data['product_type'].lower()).exists()
        if product_exists:
            raise serializers.ValidationError("This product type already exists")
        return data


class CreateProductCategorySerializer(serializers.Serializer):
    product_type = serializers.CharField(required=True)
    name = serializers.CharField(required=True)


class CreateIndustrySerializer(serializers.Serializer):
    new_industry_name = serializers.CharField(required=True)

    def validate(self, data):
        industry_exists = Industry.objects.filter(name=data['new_industry_name'].lower()).exists()
        if industry_exists:
            raise serializers.ValidationError("Industry with this name already exists")
        return data


class CreateMachineTypeSerializer(serializers.Serializer):
    machine_name = serializers.CharField(required=True)
    industry_id = serializers.CharField(required=True)

    def validate(self, data):
        industry_exists = Industry.objects.filter(id=data['industry_id']).exists()
        if not industry_exists:
            raise serializers.ValidationError("Industry id not exists")

        machine_exists = MachineType.objects.filter(name=data['machine_name'],industry_id=data['industry_id']).exists()
        if machine_exists:
            raise serializers.ValidationError("Machine with this name already exists against this industry id")
        return data


class CreateProductPlanSerializer(serializers.Serializer):

    new_plan_name = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
    is_top_seller = serializers.BooleanField(required=True)

    def validate(self, data):
        plan_exists = Plan.objects.filter(name=data['new_plan_name'].lower()).exists()
        if plan_exists:
            raise serializers.ValidationError("Plan with this name already exists")

        if data['new_plan_name'] not in ["pro", "basic","free","premium"]:
            raise serializers.ValidationError("Product plan can only be pro,basic,free or premium")

        if data['price'] not in [0, 10, 19, 29]:
            raise serializers.ValidationError("product price can only be 0,10,19 or 29")
        return data


class GetMachineTypesSerializer(serializers.Serializer):
    industry_id = serializers.IntegerField(required=True)

    def validate(self, data):
        industry_exists = MachineType.objects.filter(industry_id=data['industry_id']).exists()
        if not industry_exists:
            raise serializers.ValidationError("Industry id does not exist")
        return data
