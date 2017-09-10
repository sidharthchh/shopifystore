from models import Product


def update_products_in_db(products):
    for product in products:
        create_or_update_product(product)


def create_or_update_product(product):
    Product.objects.update_or_create(product_id=product.get('id'),
                                     defaults={
                                         'product_id': product.get('id'),
                                         'title': product.get('title'),
                                         'body_html': product.get('body_html'),
                                         'created_at': product.get('created_at'),
                                         'updated_at': product.get('updated_at'),
                                         'variants': product.get('variants'),
                                         'options': product.get('options'),
                                         'images': product.get('images'),
                                         'image': product.get('image'),
                                     })
