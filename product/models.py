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


class Transmission(models.Model):
    name = models.CharField(max_length=30)


class Fuel(models.Model):
    name = models.CharField(max_length=30)


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
    product_pics = models.ImageField(upload_to='product_images')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    patent = models.ImageField(upload_to='patent_image')
    engine_no = models.CharField(max_length=6)
    chassis_no = models.CharField(max_length=17)
    net_weight = models.FloatField(max_length=30)
    power = models.FloatField(max_length=30)
    displacement = models.FloatField(max_length=30)
    torque = models.FloatField(max_length=30)
    mixed_consumption = models.CharField(max_length=30)
    transmission = models.CharField(max_length=10)
    fuel = models.CharField(max_length=10)
    traction = models.CharField(max_length=10)
    scheduled_maintenance = models.BooleanField(null=True)
    technical_visit_included = models.BooleanField(null=True)
    is_insurance_verified = models.BooleanField(default=False)
    supply_included = models.BooleanField(null=True)
    product_condition = models.CharField(max_length=10)
    has_certificate = models.BooleanField(null=True)
    has_insurance = models.BooleanField(null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()
    product_label = models.ForeignKey(Label, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    title = models.TextField()


class Condition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_condition = models.CharField(max_length=30)
    hours_used = models.CharField(max_length=30)
    km_run = models.CharField(max_length=30)


class Insurance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='Insuranceimages')


class Certificate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    file = models.ImageField(upload_to='certificateimages')


class RentInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    hourly_rate = models.FloatField(max_length=20)
    minimum_hours = models.IntegerField()
    detailed=models.BooleanField(null=True)
    dispatch_included = models.BooleanField(default=False)
    operator_included = models.BooleanField(default=False)
    maq_lease_contract = models.BooleanField(default=False)
    lease_guaranteed_condition_checklist = models.BooleanField(default=False)
    percentage_amount = models.IntegerField()
    percentage = models.IntegerField()


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
    product_pics = models.ImageField(upload_to='productimages')


