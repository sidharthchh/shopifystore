"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout

from . import views, webhooks

# router = DefaultRouter()
# router.register(r'users', UserViewSet)

# schema_view = get_swagger_view(title='store APIs')

urlpatterns = [
    url('', include('social_django.urls', namespace='social')),
    url(r'^$', views.home),
    url(r'^login/$', views.login),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^cart/$', views.cart),
    url(r'^checkout/$', views.checkout),
    url(r'^orders/$', views.orders),
    url(r'^all_orders/$', views.all_orders),
    url(r'^admin/', admin.site.urls),
    url(r'^authenticate/$', views.authenticate),
    url(r'^product_delete/$', webhooks.product_delete),
    url(r'^product_update_create/$', webhooks.product_update_create),
    url(r'^order_delete/$', webhooks.order_delete),
    url(r'^order_update_create/$', webhooks.order_update_create),
    url(r'^create_order_for_user/$', views.create_order_for_user),
    url(r'^add_to_cart/$', views.add_to_cart),
    # url(r'^swagger/$', schema_view),
    # url(r'^api/v1/', include(authentication_urls)),
    # url(r'^api/v1/', include(router.urls)),

    url(r'^healthcheck/$', views.health_check),
]
