import json

from django.conf import settings
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
