from __future__ import unicode_literals, absolute_import

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth


def health_check(request):
    return HttpResponse("OK", status=200)


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


def authenticate(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    # authentication of the user, to check if it's active or None
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            # this is where the user login actually happens, before this the user
            # is not logged in.
            auth.login(request, user)
            return redirect('/')

    else:
        return HttpResponseRedirect("Invalid username or password")


@csrf_exempt
def webhook_products(request):
    """
    This view is used to accept the webhooks from shopify for products
    Args:
        request: request object from the webhook

    Returns: status 200

    """
    pass


@csrf_exempt
def webhook_orders(request):
    """
    This view is used to accept the webhooks from shopify for orders
    Args:
        request: request object from the webhook

    Returns: status 200

    """
    pass
