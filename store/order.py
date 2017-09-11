import requests
from django.conf import settings

from models import Order, Cart


def update_order_in_db(orders):
    """
    Update bulk order in the dictionary
    Args:
        orders: list of order 

    Returns: None

    """
    for order in orders:
        create_or_update_order(order)


def create_or_update_order(order):
    """
    A common function used to create or update an order in the repository
    Args:
        order: order json which contains all the details of order

    Returns: None

    """
    Order.objects.update_or_create(order_id=order.get('id'),
                                   defaults={
                                       'order_id': order.get('id'),
                                       'created_at': order.get('created_at'),
                                       'updated_at': order.get('updated_at'),
                                       'user_email': order.get('user_email'),
                                       'total_price': order.get('total_price'),
                                       'order_number': order.get('order_number'),
                                       'line_items': order.get('line_items')

                                   })


def create_line_items(user):
    line_items = []
    cart = Cart.objects.filter(user=user)
    for item in cart:
        line_items.append(
            {"variant_id": item.product.variants[0].get('id'),
             "quantity": 1}
        )

    return line_items


def clear_cart(user):
    Cart.objects.filter(user=user).delete()


def create_address(address, phone, city, country, state, pin, user):
    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "address1": address,
        "phone": phone,
        "city": city,
        "province": state,
        "country": country,
        "zip": pin
    }


def create_order(address, phone, city, country, state, pin, user):
    """
    create a new order and make 
    Args:
        data: details needed to place an order
        user: user object  

    Returns: None

    """
    line_items = create_line_items(user)
    payload = {
        "order": {
            "email": user.email,
            "fulfillment_status": "fulfilled",
            "send_receipt": True,
            "send_fulfillment_receipt": True,
            "line_items": line_items,
            "customer": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            },
            "billing_address": create_address(address, phone, city, country, state, pin, user),
            "shipping_address": create_address(address, phone, city, country, state, pin, user),
        }
    }
    print payload
    response = requests.post(url=settings.SHOPIFY_ORDER_URL, json=payload)
    print response.content
    # TODO: check the response and return
