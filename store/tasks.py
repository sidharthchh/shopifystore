import json

from django.conf import settings

import order
import product_helper
import request_helper
from store.celery import app


@app.task
def fetch_products_from_shopify():
    """
    Celery task to fetch the products for once.
    This is just done once as we are using webhooks.
    
    Returns: None

    """
    response = request_helper.get_request(url=settings.SHOPIFY_PRODUCT_URL)
    products = json.loads(response.content).get('products', [])
    product_helper.update_products_in_db(products)


@app.task
def fetch_orders_from_shopify():
    """
    Celery task to fetch the orders for once.
    This is just done once as we are using webhooks.

    Returns: None

    """
    response = request_helper.get_request(url=settings.SHOPIFY_ORDER_URL)
    orders = json.loads(response.content).get('orders', [])
    order.update_order_in_db(orders)
