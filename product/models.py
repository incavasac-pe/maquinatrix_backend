from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=30,unique=True)


class Model(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class Year(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.CharField(max_length=30)


class Label(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)


class Region(models.Model):
    name = models.CharField(max_length=30)


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=30,unique=True)

    class Meta:
        unique_together = ('region_id', 'city_name')


class Plan(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    is_top_seller = models.BooleanField(default=False)


class Industry(models.Model):
    name = models.CharField(max_length=30)


class MachineType(models.Model):
    name = models.CharField(max_length=30)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)


class ProductType(models.Model):
    name = models.CharField(max_length=30,unique=True)


class ProductCategories(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class Product(models.Model):

    status = models.CharField(default="draft",max_length=20)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    product_category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='product_images',null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE,null=True)
    patent = models.ImageField(upload_to='patent_image',null=True)
    engine_no = models.CharField(max_length=6,null=True)
    chassis_no = models.CharField(max_length=17,null=True)
    net_weight = models.FloatField(max_length=30,null=True)
    power = models.FloatField(max_length=30,null=True)
    displacement = models.FloatField(max_length=30,null=True)
    torque = models.FloatField(max_length=30,null=True)
    mixed_consumption = models.CharField(max_length=30,null=True)
    transmission = models.CharField(max_length=10,null=True)
    fuel = models.CharField(max_length=10,null=True)
    traction = models.CharField(max_length=10,null=True)
    scheduled_maintenance = models.BooleanField(null=True)
    technical_visit_included = models.BooleanField(null=True)
    is_insurance_verified = models.BooleanField(default=False,null=True)
    supply_included = models.BooleanField(null=True)
    product_condition = models.CharField(max_length=10,null=True)
    has_certificate = models.BooleanField(null=True,)
    has_insurance = models.BooleanField(null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
    description = models.TextField(null=True)
    product_label = models.ForeignKey(Label, on_delete=models.CASCADE,null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


class Condition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_condition = models.CharField(max_length=30,null=True)
    hours_used = models.CharField(max_length=10,null=True)
    km_run = models.CharField(max_length=30,null=True)


class Insurance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='insurance-images')


class Certificate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    file = models.ImageField(upload_to='certificate-images')


class RentInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    hourly_rate = models.FloatField(max_length=20,null=True)
    minimum_hours = models.IntegerField(null=True)
    detailed=models.BooleanField(null=True)
    dispatch_included = models.BooleanField(null=True)
    operator_included = models.BooleanField(null=True)
    maq_lease_contract = models.BooleanField(null=True)
    lease_guaranteed_condition_checklist = models.BooleanField(null=True)
    percentage_amount = models.IntegerField(null=True)
    percentage = models.IntegerField(null=True)


class RentDetailed(models.Model):
    rent = models.ForeignKey(RentInfo, on_delete=models.CASCADE)
    value_1 = models.IntegerField()
    value_2 = models.IntegerField()
    value_3 = models.IntegerField()
    value_4 = models.IntegerField()
    value_5 = models.IntegerField()
    value_6 = models.IntegerField()
    value_7 = models.IntegerField()
    value_8 = models.IntegerField()
    value_9 = models.IntegerField()


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_pics = models.ImageField(upload_to='product-images')


