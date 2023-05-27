from .products_serializers import ProductImagesSerializer
from .models import Condition, RentInfo, Certificate,Insurance,Product,ProductImages
from maquinatrix_backend.services import modify_input_for_multiple_files


def create_machinery_and_vehicles_rent(serializer,data):
    brand_id = serializer.validated_data.get('brand_id')
    model_id = serializer.validated_data.get('model_id')
    year_id = serializer.validated_data.get('year_id')
    patent = serializer.validated_data.get('patent')
    product_type_id = serializer.validated_data.get('product_type_id')
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
    cover_image = serializer.validated_data['cover_image']
    product_label_id = serializer.validated_data.get('product_label_id')
    city_id = serializer.validated_data.get('city_id')
    region_id = serializer.validated_data.get('region_id')
    product_pics = dict((data).lists())['product_pics']
    product_obj = Product.objects.create(product_type_id=product_type_id,
                                         product_category_id=category_type_id,
                                         cover_image=cover_image,
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
                                         product_label=product_label_id,
                                         plan_id=plan_id,
                                         title=title,
                                         industry_id=industry_id,
                                         machine_type_id=machine_type_id)

    product_id = product_obj.id
    if product_condition:
        if product_condition == "used":
            if product_hours or product_km:
                Condition.objects.create(product_id=product_id, product_condition=product_condition,
                                             hours_used=product_hours,
                                             km_run=product_km)
    if has_insurance:
        if insurance_doc:
            Insurance.objects.create(file=insurance_doc, product_id=product_id)
    if has_certificate:
        if certificate_date or certificate_doc:
            Certificate.objects.create(date=certificate_date, file=certificate_doc, product_id=product_id)

    if hourly_rate or minimum_hours or detailed or dispatch_included or operator_included or \
            maq_lease_contract or lease_guaranteed_condition_checklist or percentage_amount or percentage:
        RentInfo.objects.create(product_id=product_id,
                                hourly_rate=hourly_rate,
                                minimum_hours=minimum_hours,
                                detailed=detailed,
                                dispatch_included=dispatch_included,
                                operator_included=operator_included,
                                maq_lease_contract=maq_lease_contract,
                                lease_guaranteed_condition_checklist=lease_guaranteed_condition_checklist,
                                percentage_amount=percentage_amount,
                                percentage=percentage
                                )

    if product_pics:
        for img_name in product_pics:
            modified_data = modify_input_for_multiple_files(product_id, img_name)
            file_serializer = ProductImagesSerializer(data=modified_data)
            if file_serializer.is_valid():
                product_id = file_serializer.validated_data.get('product_id')
                product_pics = file_serializer.validated_data.get('product_pics')
                ProductImages.objects.create(product_id=product_id,
                                             product_pics=product_pics)

    return product_obj
