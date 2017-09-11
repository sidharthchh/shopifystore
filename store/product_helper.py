from models import Product


def update_products_in_db(products):
    """
    update bulk product into the db
    Args:
        products: list of products

    Returns: None

    """
    for product in products:
        create_or_update_product(product)


def create_or_update_product(product):
    """
    To create or update a product
    Args:
        product: product details

    Returns: None

    """
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


def delete_product(product_id):
    """
    Method to delete a product. 
    Here we need not have a try except as we are using filter
    Args:
        product_id: to delete a product

    Returns: None

    """
    Product.objects.filter(product_id=product_id).delete()
