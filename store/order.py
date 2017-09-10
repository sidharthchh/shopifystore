from models import Order


def update_order_in_db(orders):
    for order in orders:
        create_or_update_order(order)


def create_or_update_order(order):
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
