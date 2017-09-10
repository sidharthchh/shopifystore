from .common import *

# CELERY
# In development, all tasks will be executed locally by blocking until the task returns
# CELERY_ALWAYS_EAGER = True
# END CELERY

# SHOPIFY DETAILS
SHOPIFY_API_KEY = os.environ.get("SHOPIFY_API_KEY")
SHOPIFY_PASSWORD = os.environ.get("SHOPIFY_PASSWORD")
SHOPIFY_HOSTNAME = os.environ.get("SHOPIFY_HOSTNAME")
SHOPIFY_BASE_URL = "https://{}:{}@{}".format(SHOPIFY_API_KEY, SHOPIFY_PASSWORD, SHOPIFY_HOSTNAME)
SHOPIFY_PRODUCT_URL = SHOPIFY_BASE_URL + "/admin/products.json"
SHOPIFY_ORDER_URL = SHOPIFY_BASE_URL + "/admin/orders.json"
