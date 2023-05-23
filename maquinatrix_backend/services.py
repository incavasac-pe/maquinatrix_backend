from rest_framework import status


def success_response(status_code=None, data=None, msg='Operation Success!'):
    response = {
        'status_code': status_code,
        'success': True,
        'message': msg,
        'data': data
    }
    if not status_code:
        # pass
        response["status_code"] = status.HTTP_200_OK
    return response


def failure_response(status_code=None, errors=None, msg='Operation Failure'):
    response = {
        'status_code': status_code,
        'success': False,
        'message': msg,
        'errors': errors
    }
    if not status_code:
        # pass
        response["status_code"] = status.HTTP_400_BAD_REQUEST
    return response


sale_categories = ["machine and vehicles","equipments and tools", "product and accessories","requests","tire"]
rent_categories = ["machine and vehicles","equipments and tools"]

product_types = ["rent","sale"]

label_types=["opportunity","offer","new","pre-owned","liquidation"]
label_price=[3,3,5,3,3]

plan_types=["free","basic","pro","premium"]
plan_prices=[0,10,19,29]
plan_seller=["False","False","True","False"]


def modify_input_for_multiple_files(product_id, product_pics):
    dict = {}
    dict['product_id'] = product_id
    dict['product_pics'] = product_pics
    return dict


