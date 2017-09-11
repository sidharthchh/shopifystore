import json

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from order import delete_order, create_or_update_order
from product_helper import create_or_update_product, delete_product


@csrf_exempt
def product_delete(request):
    """
    This view is used to accept the webhooks from shopify for products
    Args:
        request: request object from the webhook

    Returns: status 200

    """
    product = json.loads(request.body)
    product_id = product.get('id')
    delete_product(product_id)
    return HttpResponse("OK", status=200)


@csrf_exempt
def product_update_create(request):
    """
    This view is used to accept the webhooks from shopify for products
    Args:
        request: request object from the webhook

    Returns: status 200

    """
    product = json.loads(request.body)
    create_or_update_product(product)
    return HttpResponse("OK", status=200)


@csrf_exempt
def order_delete(request):
    """
    This view is used to accept the webhooks from shopify for products
    Args:
        request: request object from the webhook

    Returns: status 200

    """
    order = json.loads(request.body)
    order_id = order.get('id')
    delete_order(order_id)
    return HttpResponse("OK", status=200)


@csrf_exempt
def order_update_create(request):
    """
    This view is used to accept the webhooks from shopify for products
    Args:
        request: request object from the webhook

    Returns: status 200

    """
    order = json.loads(request.body)
    create_or_update_order(order)
    return HttpResponse("OK", status=200)
