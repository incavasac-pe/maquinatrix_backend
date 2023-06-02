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


class CreateSizeSerializer(serializers.Serializer):
    new_tyre_size = serializers.IntegerField(required=True)
    def validate(self, data):
        """
        Check new_brand_name is valid
        """

        size_id_exists = Size.objects.filter(name=data['new_tyre_size']).exists()
        if size_id_exists:
            raise serializers.ValidationError("Size already exists")
        else:
            return data

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'


class ProductPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'


class ProductCategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategories
        fields = '__all__'

class TyresSerializer(serializers.ModelSerializer):

    class Meta:
        model = TyresInfo
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


class ProductSerializerById(serializers.Serializer):
   user_id = serializers.IntegerField(required=True)


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


class MachineryAndVehiclesRentSerializer(serializers.Serializer):
    product_type_id = serializers.CharField(required=True)
    product_pics = serializers.ImageField(required=True)
    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.IntegerField(required=True)
    year_id = serializers.IntegerField(required=False)
    patent = serializers.ImageField(required=False)
    engine_no = serializers.CharField(required=False)
    chassis_no = serializers.CharField(required=False)
    net_weight = serializers.FloatField(required=False)
    power = serializers.FloatField(required=False)
    displacement = serializers.FloatField(required=False)
    torque = serializers.FloatField(required=False)
    mixed_consumption = serializers.CharField(required=False)
    transmission = serializers.CharField(required=False)
    fuel = serializers.CharField(required=False)
    traction = serializers.CharField(required=False)
    scheduled_maintenance = serializers.BooleanField(required=False)
    technical_visit_included = serializers.BooleanField(required=False)
    supply_included = serializers.BooleanField(required=False)
    product_condition = serializers.CharField(required=False)
    product_hours = serializers.IntegerField(required=False,)
    product_km = serializers.CharField(required=False,)
    has_certificate = serializers.BooleanField(required=False)
    has_insurance = serializers.BooleanField(required=False)
    region_id = serializers.CharField(required=False)
    city_id = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    product_label_id = serializers.IntegerField(required=False)
    certificate_date = serializers.DateField(required=False)
    insurance_doc = serializers.ImageField(required=False)
    certificate_doc = serializers.ImageField(required=False)
    hourly_rate = serializers.IntegerField(required=False)
    minimum_hours = serializers.IntegerField(required=False)
    detailed_fee_scheduele = serializers.BooleanField(required=False)
    dispatch_included = serializers.CharField(required=False)
    operator_included = serializers.CharField(required=False)
    maq_lease_contract = serializers.CharField(required=False)
    lease_guaranteed_condition_checklist = serializers.CharField(required=False)
    percentage_amount = serializers.IntegerField(required=False)
    percentage = serializers.IntegerField(required=False)
    product_plan_id = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    product_category_id=serializers.CharField(required=True)
    industry_id=serializers.IntegerField(required=True)
    machine_type_id=serializers.IntegerField(required=True)
    cover_image = serializers.ImageField(required=False)




    def validate(self, data):

        if 'fuel' in data:
            if data['fuel'] not in ["diesel", "benzine", "not classified"]:
                raise serializers.ValidationError("fuel must be diesel, benzine or not classified")

        if 'product_condition' in data:
            if data['product_condition'] not in ["new", "used"]:
                raise serializers.ValidationError("product_condition must be new or used")

        if 'transmission' in data:
            if data['transmission'] not in ["manual", "automatic","not classified"]:
                raise serializers.ValidationError("transmission must be manual, automatic or not classified")

        if 'brand_id' not in data:
            raise serializers.ValidationError("brand_id can not be empty")
        else:
            brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
            if not brand_id_exists:
                raise serializers.ValidationError("This brand id not present in db")

        if 'year_id' in data:
            year_id_exists = Year.objects.filter(id=data['year_id']).exists()
            if not year_id_exists:
                raise serializers.ValidationError("This year id not present in db")

        if 'model_id' in data:
            model_id_exists = Model.objects.filter(id=data['model_id']).exists()
            if not model_id_exists:
                raise serializers.ValidationError("This model id not present in db")

        if 'region_id' in data:
            region_id_exists = Region.objects.filter(id=data['region_id']).exists()
            if not region_id_exists:
                raise serializers.ValidationError("This region id not present in db")

        if 'city_id' in data:
            city_id_exists = City.objects.filter(id=data['city_id']).exists()
            if not city_id_exists:
                raise serializers.ValidationError("This city id not present in db")

        if 'industry_id' in data:
            industry_id_exists = Industry.objects.filter(id=data['industry_id']).exists()
            if not industry_id_exists:
                raise serializers.ValidationError("This industry id not present in db")

        if 'machine_type_id' in data:
            machine_type_id_exists = MachineType.objects.filter(id=data['machine_type_id']).exists()
            if not machine_type_id_exists:
                raise serializers.ValidationError("This machine type id not present in db")

        if 'product_category_id' in data:
            product_cat_id_exists = ProductCategories.objects.filter(id=data['product_category_id']).exists()
            if not product_cat_id_exists:
                raise serializers.ValidationError("This product category id not present in db")

        if 'product_plan_id' in data:
            product_plan_id_exists = Plan.objects.filter(id=data['product_plan_id']).exists()
            if not product_plan_id_exists:
                raise serializers.ValidationError("This product plan id id not present in db")

        if 'product_label_id' in data:
            product_label_id_exists = Label.objects.filter(id=data['product_label_id']).exists()
            if not product_label_id_exists:
                raise serializers.ValidationError("This label id not present in db")

        if 'product_type_id' in data:
            product_type_id_exists = ProductType.objects.filter(id=data['product_type_id']).exists()
            if not product_type_id_exists:
                raise serializers.ValidationError("This product type id not present in db")
        return data


class MachineryAndVehiclesSaleSerializer(serializers.Serializer):
    product_type_id = serializers.CharField(required=True)
    product_pics = serializers.ImageField(required=True)
    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.IntegerField(required=True)
    region_id = serializers.CharField(required=True)
    city_id = serializers.CharField(required=True)
    dispatch_included = serializers.CharField(required=True)
    product_plan_id = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    product_category_id = serializers.CharField(required=True)
    industry_id = serializers.IntegerField(required=True)
    machine_type_id = serializers.IntegerField(required=True)
    product_condition = serializers.CharField(required=True)
    product_price = serializers.IntegerField(required=True)
    year_id = serializers.IntegerField(required=False)
    patent = serializers.ImageField(required=False)
    engine_no = serializers.CharField(required=False)
    chassis_no = serializers.CharField(required=False)
    net_weight = serializers.FloatField(required=False)
    power = serializers.FloatField(required=False)
    displacement = serializers.FloatField(required=False)
    torque = serializers.FloatField(required=False)
    mixed_consumption = serializers.CharField(required=False)
    transmission = serializers.CharField(required=False)
    fuel = serializers.CharField(required=False)
    traction = serializers.CharField(required=False)
    product_hours = serializers.IntegerField(required=False)
    product_km = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    product_label_id = serializers.IntegerField(required=False)
    cover_image = serializers.ImageField(required=False)

    def validate(self, data):
        if 'fuel' in data:
            if data['fuel'] not in ["diesel", "benzine", "not classified"]:
                raise serializers.ValidationError("fuel must be diesel, benzine or not classified")

        if 'product_condition' in data:
            if data['product_condition'] not in ["new", "used"]:
                raise serializers.ValidationError("product_condition must be new or used")

        if 'transmission' in data:
            if data['transmission'] not in ["manual", "automatic","not classified"]:
                raise serializers.ValidationError("transmission must be manual, automatic or not classified")

        if 'brand_id' not in data:
            raise serializers.ValidationError("brand_id can not be empty")
        else:
            brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
            if not brand_id_exists:
                raise serializers.ValidationError("This brand id not present in db")

        if 'year_id' in data:
            year_id_exists = Year.objects.filter(id=data['year_id']).exists()
            if not year_id_exists:
                raise serializers.ValidationError("This year id not present in db")

        if 'model_id' in data:
            model_id_exists = Model.objects.filter(id=data['model_id']).exists()
            if not model_id_exists:
                raise serializers.ValidationError("This model id not present in db")

        region_id_exists = Region.objects.filter(id=data['region_id']).exists()
        if not region_id_exists:
            raise serializers.ValidationError("This region id not present in db")

        city_id_exists = City.objects.filter(id=data['city_id']).exists()
        if not city_id_exists:
            raise serializers.ValidationError("This city id not present in db")

        industry_id_exists = Industry.objects.filter(id=data['industry_id']).exists()
        if not industry_id_exists:
            raise serializers.ValidationError("This industry id not present in db")

        machine_type_id_exists = MachineType.objects.filter(id=data['machine_type_id']).exists()
        if not machine_type_id_exists:
            raise serializers.ValidationError("This machine type id not present in db")

        product_cat_id_exists = ProductCategories.objects.filter(id=data['product_category_id']).exists()
        if not product_cat_id_exists:
            raise serializers.ValidationError("This product category id not present in db")

        product_plan_id_exists = Plan.objects.filter(id=data['product_plan_id']).exists()
        if not product_plan_id_exists:
            raise serializers.ValidationError("This product plan id id not present in db")

        if 'product_label_id' in data:
            product_label_id_exists = Label.objects.filter(id=data['product_label_id']).exists()
            if not product_label_id_exists:
                raise serializers.ValidationError("This label id not present in db")

        product_type_id_exists = ProductType.objects.filter(id=data['product_type_id']).exists()
        if not product_type_id_exists:
            raise serializers.ValidationError("This product type id not present in db")
        return data


class ProductAndAccessoriesSaleSerializer(serializers.Serializer):
    product_type_id = serializers.CharField(required=True)
    product_pics = serializers.ImageField(required=True)
    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.IntegerField(required=True)
    region_id = serializers.CharField(required=True)
    city_id = serializers.CharField(required=True)
    dispatch_included = serializers.CharField(required=True)
    product_condition = serializers.CharField(required=True)
    product_plan_id = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    product_category_id = serializers.CharField(required=True)
    industry_id = serializers.IntegerField(required=True)
    machine_type_id = serializers.IntegerField(required=True)
    part_number = serializers.CharField(required=True)
    product_price = serializers.IntegerField(required=True)
    year_id = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    product_label_id = serializers.IntegerField(required=False)
    cover_image = serializers.ImageField(required=False)

    def validate(self, data):
        if 'product_condition' in data:
            if data['product_condition'] not in ["new", "used"]:
                raise serializers.ValidationError("product_condition must be new or used")

        brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
        if not brand_id_exists:
            raise serializers.ValidationError("This brand id not present in db")

        if 'year_id' in data:
            year_id_exists = Year.objects.filter(id=data['year_id']).exists()
            if not year_id_exists:
                raise serializers.ValidationError("This year id not present in db")

        model_id_exists = Model.objects.filter(id=data['model_id']).exists()
        if not model_id_exists:
            raise serializers.ValidationError("This model id not present in db")

        if 'region_id' in data:
            region_id_exists = Region.objects.filter(id=data['region_id']).exists()
            if not region_id_exists:
                raise serializers.ValidationError("This region id not present in db")

        if 'city_id' in data:
            city_id_exists = City.objects.filter(id=data['city_id']).exists()
            if not city_id_exists:
                raise serializers.ValidationError("This city id not present in db")

        industry_id_exists = Industry.objects.filter(id=data['industry_id']).exists()
        if not industry_id_exists:
            raise serializers.ValidationError("This industry id not present in db")

        machine_type_id_exists = MachineType.objects.filter(id=data['machine_type_id']).exists()
        if not machine_type_id_exists:
            raise serializers.ValidationError("This machine type id not present in db")

        product_cat_id_exists = ProductCategories.objects.filter(id=data['product_category_id']).exists()
        if not product_cat_id_exists:
            raise serializers.ValidationError("This product category id not present in db")

        if 'product_plan_id' in data:
            product_plan_id_exists = Plan.objects.filter(id=data['product_plan_id']).exists()
            if not product_plan_id_exists:
                raise serializers.ValidationError("This product plan id id not present in db")

        if 'product_label_id' in data:
            product_label_id_exists = Label.objects.filter(id=data['product_label_id']).exists()
            if not product_label_id_exists:
                raise serializers.ValidationError("This label id not present in db")

        product_type_id_exists = ProductType.objects.filter(id=data['product_type_id']).exists()
        if not product_type_id_exists:
            raise serializers.ValidationError("This product type id not present in db")

        return data


class ReplacementPartsSaleSerializer(serializers.Serializer):
    product_type_id = serializers.CharField(required=True)
    product_pics = serializers.ImageField(required=True)
    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.IntegerField(required=True)
    year_id = serializers.IntegerField(required=True)
    dispatch_included = serializers.CharField(required=True)
    product_plan_id = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    product_condition = serializers.CharField(required=True)
    product_category_id = serializers.CharField(required=True)
    industry_id = serializers.IntegerField(required=True)
    machine_type_id = serializers.IntegerField(required=True)
    region_id = serializers.CharField(required=True)
    city_id = serializers.CharField(required=True)
    part_number = serializers.CharField(required=True)
    product_price = serializers.IntegerField(required=True)
    engine_no = serializers.CharField(required=False)
    chassis_no = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    product_label_id = serializers.IntegerField(required=False)
    cover_image = serializers.ImageField(required=False)


    def validate(self, data):

        if data['product_condition'] not in ["new", "used"]:
            raise serializers.ValidationError("product condition must be new or used")

        brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
        if not brand_id_exists:
                raise serializers.ValidationError("This brand id not present in db")

        year_id_exists = Year.objects.filter(id=data['year_id']).exists()
        if not year_id_exists:
                raise serializers.ValidationError("This year id not present in db")

        if 'model_id' in data:
            model_id_exists = Model.objects.filter(id=data['model_id']).exists()
            if not model_id_exists:
                raise serializers.ValidationError("This model id not present in db")

        region_id_exists = Region.objects.filter(id=data['region_id']).exists()
        if not region_id_exists:
                raise serializers.ValidationError("This region id not present in db")

        city_id_exists = City.objects.filter(id=data['city_id']).exists()
        if not city_id_exists:
                raise serializers.ValidationError("This city id not present in db")

        industry_id_exists = Industry.objects.filter(id=data['industry_id']).exists()
        if not industry_id_exists:
                raise serializers.ValidationError("This industry id not present in db")

        machine_type_id_exists = MachineType.objects.filter(id=data['machine_type_id']).exists()
        if not machine_type_id_exists:
                raise serializers.ValidationError("This machine type id not present in db")

        if 'product_category_id' in data:
            product_cat_id_exists = ProductCategories.objects.filter(id=data['product_category_id']).exists()
            if not product_cat_id_exists:
                raise serializers.ValidationError("This product category id not present in db")

        if 'product_plan_id' in data:
            product_plan_id_exists = Plan.objects.filter(id=data['product_plan_id']).exists()
            if not product_plan_id_exists:
                raise serializers.ValidationError("This product plan id id not present in db")

        if 'product_label_id' in data:
            product_label_id_exists = Label.objects.filter(id=data['product_label_id']).exists()
            if not product_label_id_exists:
                raise serializers.ValidationError("This label id not present in db")

        if 'product_type_id' in data:
            product_type_id_exists = ProductType.objects.filter(id=data['product_type_id']).exists()
            if not product_type_id_exists:
                raise serializers.ValidationError("This product type id not present in db")
        return data


class EquipmentAndToolsSaleSerializer(serializers.Serializer):
    product_type_id = serializers.CharField(required=True)
    product_pics = serializers.ImageField(required=True)
    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.IntegerField(required=True)
    product_price = serializers.IntegerField(required=True)
    dispatch_included = serializers.CharField(required=True)
    region_id = serializers.CharField(required=True)
    city_id = serializers.CharField(required=True)
    product_condition = serializers.CharField(required=True)
    product_plan_id = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    product_category_id = serializers.CharField(required=True)
    industry_id=serializers.IntegerField(required=True)
    machine_type_id=serializers.IntegerField(required=True)
    year_id = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)
    product_label_id = serializers.IntegerField(required=False)
    cover_image = serializers.ImageField(required=False)
    fuel = serializers.CharField(required=False)
    product_hours = serializers.IntegerField(required=False)
    product_km = serializers.CharField(required=False)


    def validate(self, data):
        if 'fuel' in data:
            if data['fuel'] not in ["diesel", "benzine", "not classified"]:
                raise serializers.ValidationError("fuel must be diesel, benzine or not classified")

        if data['product_condition'] not in ["new", "used"]:
            raise serializers.ValidationError("product condition must be new or used")

        brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
        if not brand_id_exists:
            raise serializers.ValidationError("This brand id not present in db")

        if 'year_id' in data:
            year_id_exists = Year.objects.filter(id=data['year_id']).exists()
            if not year_id_exists:
                raise serializers.ValidationError("This year id not present in db")

        model_id_exists = Model.objects.filter(id=data['model_id']).exists()
        if not model_id_exists:
            raise serializers.ValidationError("This model id not present in db")

        region_id_exists = Region.objects.filter(id=data['region_id']).exists()
        if not region_id_exists:
            raise serializers.ValidationError("This region id not present in db")

        city_id_exists = City.objects.filter(id=data['city_id']).exists()
        if not city_id_exists:
            raise serializers.ValidationError("This city id not present in db")

        industry_id_exists = Industry.objects.filter(id=data['industry_id']).exists()
        if not industry_id_exists:
            raise serializers.ValidationError("This industry id not present in db")

        machine_type_id_exists = MachineType.objects.filter(id=data['machine_type_id']).exists()
        if not machine_type_id_exists:
            raise serializers.ValidationError("This machine type id not present in db")

        if 'product_category_id' in data:
            product_cat_id_exists = ProductCategories.objects.filter(id=data['product_category_id']).exists()
            if not product_cat_id_exists:
                raise serializers.ValidationError("This product category id not present in db")

        if 'product_plan_id' in data:
            product_plan_id_exists = Plan.objects.filter(id=data['product_plan_id']).exists()
            if not product_plan_id_exists:
                raise serializers.ValidationError("This product plan id id not present in db")

        if 'product_label_id' in data:
            product_label_id_exists = Label.objects.filter(id=data['product_label_id']).exists()
            if not product_label_id_exists:
                raise serializers.ValidationError("This label id not present in db")

        if 'product_type_id' in data:
            product_type_id_exists = ProductType.objects.filter(id=data['product_type_id']).exists()
            if not product_type_id_exists:
                raise serializers.ValidationError("This product type id not present in db")
        return data


class TyreSerializer(serializers.Serializer):
    product_pics = serializers.ImageField(required=True)
    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.IntegerField(required=True)
    product_condition = serializers.CharField(required=True)
    dispatch_included = serializers.CharField(required=True)
    region_id = serializers.CharField(required=True)
    city_id = serializers.CharField(required=True)
    product_plan_id = serializers.CharField(required=True)
    product_category_id = serializers.CharField(required=True)
    product_price = serializers.IntegerField(required=True)
    section_width = serializers.IntegerField(required=True)
    aspect_ratio = serializers.CharField(required=True)
    load_index = serializers.FloatField(required=True)
    speed_index = serializers.FloatField(required=True)
    product_type_id = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    product_label_id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    industry_id=serializers.IntegerField(required=False)
    machine_type_id=serializers.IntegerField(required=False)
    cover_image = serializers.ImageField(required=False)
    size_id = serializers.IntegerField(required=False)
    tire_diameter = serializers.FloatField(required=True)
    outside_diameter = serializers.FloatField(required=True)
    maximum_load = serializers.FloatField(required=False)
    maximum_speed = serializers.FloatField(required=False)
    utqg = serializers.CharField(required=False)
    wear_rate = serializers.CharField(required=False)
    traction_index = serializers.CharField(required=False)
    temperature_index = serializers.CharField(required=False)
    type_of_construction = serializers.CharField(required=False)
    is_run_flat = serializers.BooleanField(required=False)
    terrain_type_condition = serializers.CharField(required=False)
    terrain_type_technology = serializers.CharField(required=False)
    tread_design_technology = serializers.CharField(required=False)
    type_of_service_condition = serializers.CharField(required=True)
    vehicle_type_condition = serializers.CharField(required=True)
    season_condition = serializers.CharField(required=False)

    def validate(self, data):
        if data['product_condition'] not in ["new", "used"]:
            raise serializers.ValidationError("product condition must be new or used")

        if 'season_condition' in data:
            if data['season_condition'] not in ["winter", "summer", "all season"]:
                raise serializers.ValidationError("season_condition must be winter or summer or all season")

        if 'size_id' in data:
            size_id_exists = Size.objects.filter(id=data['size_id']).exists()
            if not size_id_exists:
                raise serializers.ValidationError("This size id not present in db")

        brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
        if not brand_id_exists:
            raise serializers.ValidationError("This brand id not present in db")

        model_id_exists = Model.objects.filter(id=data['model_id']).exists()
        if not model_id_exists:
            raise serializers.ValidationError("This model id not present in db")

        region_id_exists = Region.objects.filter(id=data['region_id']).exists()
        if not region_id_exists:
            raise serializers.ValidationError("This region id not present in db")

        city_id_exists = City.objects.filter(id=data['city_id']).exists()
        if not city_id_exists:
            raise serializers.ValidationError("This city id not present in db")

        industry_id_exists = Industry.objects.filter(id=data['industry_id']).exists()
        if not industry_id_exists:
            raise serializers.ValidationError("This industry id not present in db")

        machine_type_id_exists = MachineType.objects.filter(id=data['machine_type_id']).exists()
        if not machine_type_id_exists:
            raise serializers.ValidationError("This machine type id not present in db")

        product_cat_id_exists = ProductCategories.objects.filter(id=data['product_category_id']).exists()
        if not product_cat_id_exists:
            raise serializers.ValidationError("This product category id not present in db")

        product_plan_id_exists = Plan.objects.filter(id=data['product_plan_id']).exists()
        if not product_plan_id_exists:
            raise serializers.ValidationError("This product plan id id not present in db")

        if 'product_label_id' in data:
            product_label_id_exists = Label.objects.filter(id=data['product_label_id']).exists()
            if not product_label_id_exists:
                raise serializers.ValidationError("This label id not present in db")

        product_type_id_exists = ProductType.objects.filter(id=data['product_type_id']).exists()
        if not product_type_id_exists:
            raise serializers.ValidationError("This product type id not present in db")

        return data


class EquipmentAndToolsRentSerializer(serializers.Serializer):
    product_type_id = serializers.CharField(required=True)
    product_plan_id = serializers.CharField(required=True)
    title = serializers.CharField(required=True)
    product_category_id = serializers.CharField(required=True)
    industry_id = serializers.IntegerField(required=True)
    machine_type_id = serializers.IntegerField(required=True)
    brand_id = serializers.IntegerField(required=True)
    model_id = serializers.IntegerField(required=True)
    product_condition = serializers.CharField(required=True)
    product_pics = serializers.ImageField(required=False)
    year_id = serializers.IntegerField(required=False)
    net_weight = serializers.FloatField(required=False)
    power = serializers.FloatField(required=False)
    displacement = serializers.FloatField(required=False)
    torque = serializers.FloatField(required=False)
    mixed_consumption = serializers.CharField(required=False)
    transmission = serializers.CharField(required=False)
    fuel = serializers.CharField(required=False)
    traction = serializers.CharField(required=False)
    scheduled_maintenance = serializers.BooleanField(required=False)
    technical_visit_included = serializers.BooleanField(required=False)
    supply_included = serializers.BooleanField(required=False)
    product_hours = serializers.IntegerField(required=False)
    product_km = serializers.CharField(required=False)
    has_certificate = serializers.BooleanField(required=False)
    has_insurance = serializers.BooleanField(required=False)
    region_id = serializers.CharField(required=False)
    city_id = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    product_label_id = serializers.IntegerField(required=False)
    certificate_date = serializers.DateField(required=False)
    insurance_doc = serializers.ImageField(required=False)
    certificate_doc = serializers.ImageField(required=False)
    hourly_rate = serializers.IntegerField(required=False)
    minimum_hours = serializers.IntegerField(required=False)
    detailed = serializers.BooleanField(required=False)
    dispatch_included = serializers.CharField(required=False)
    operator_included = serializers.CharField(required=False)
    maq_lease_contract = serializers.CharField(required=False)
    lease_guaranteed_condition_checklist = serializers.CharField(required=False)
    percentage_amount = serializers.IntegerField(required=False)
    percentage = serializers.IntegerField(required=False)
    cover_image = serializers.ImageField(required=False)

    def validate(self, data):
        if 'fuel' in data:
            if data['fuel'] not in ["diesel", "benzine", "not classified"]:
                raise serializers.ValidationError("fuel must be diesel, benzine or not classified")

        if data['product_condition'] not in ["new", "used"]:
            raise serializers.ValidationError("product condition must be new or used")

        if 'transmission' in data:
            if data['transmission'] not in ["manual", "automatic","not classified"]:
                raise serializers.ValidationError("transmission must be manual, automatic or not classified")

        if 'brand_id' not in data:
            raise serializers.ValidationError("brand id can not be empty")
        else:
            brand_id_exists = Brand.objects.filter(id=data['brand_id']).exists()
            if not brand_id_exists:
                raise serializers.ValidationError("This brand id not present in db")

        if 'year_id' in data:
            year_id_exists = Year.objects.filter(id=data['year_id']).exists()
            if not year_id_exists:
                raise serializers.ValidationError("This year id not present in db")

        if 'model_id' in data:
            model_id_exists = Model.objects.filter(id=data['model_id']).exists()
            if not model_id_exists:
                raise serializers.ValidationError("This model id not present in db")

        if 'region_id' in data:
            region_id_exists = Region.objects.filter(id=data['region_id']).exists()
            if not region_id_exists:
                raise serializers.ValidationError("This region id not present in db")

        if 'city_id' in data:
            city_id_exists = City.objects.filter(id=data['city_id']).exists()
            if not city_id_exists:
                raise serializers.ValidationError("This city id not present in db")

        if 'industry_id' in data:
            industry_id_exists = Industry.objects.filter(id=data['industry_id']).exists()
            if not industry_id_exists:
                raise serializers.ValidationError("This industry id not present in db")

        if 'machine_type_id' in data:
            machine_type_id_exists = MachineType.objects.filter(id=data['machine_type_id']).exists()
            if not machine_type_id_exists:
                raise serializers.ValidationError("This machine type id not present in db")

        if 'product_category_id' in data:
            product_cat_id_exists = ProductCategories.objects.filter(id=data['product_category_id']).exists()
            if not product_cat_id_exists:
                raise serializers.ValidationError("This product category id not present in db")

        if 'product_plan_id' in data:
            product_plan_id_exists = Plan.objects.filter(id=data['product_plan_id']).exists()
            if not product_plan_id_exists:
                raise serializers.ValidationError("This product plan id id not present in db")

        if 'product_label_id' in data:
            product_label_id_exists = Label.objects.filter(id=data['product_label_id']).exists()
            if not product_label_id_exists:
                raise serializers.ValidationError("This label id not present in db")

        if 'product_type_id' in data:
            product_type_id_exists = ProductType.objects.filter(id=data['product_type_id']).exists()
            if not product_type_id_exists:
                raise serializers.ValidationError("This product type id not present in db")
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
