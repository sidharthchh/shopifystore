from __future__ import unicode_literals, absolute_import

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from store.models import Product, Cart
from store.order import create_order, clear_cart


def health_check(request):
    return HttpResponse("OK", status=200)


def login(request):
    return render(request, 'login.html')


def checkout(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'checkout.html', {"cart_items": cart, "cart_no": cart.count()})


@login_required
def cart(request):
    """
    Return login page
    Args:
        request: 

    Returns:

    """
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {"cart_items": cart, "cart_no": cart.count()})


@login_required
def home(request):
    """
    return home page
    Args:
        request: 

    Returns:

    """
    cart = Cart.objects.filter(user=request.user).values_list('product__id', flat=True)
    cart_no = cart.count()
    products = Product.objects.all()
    return render(request, 'index.html', {"products": products, "cart": cart_no,
                                          "cart_items": cart})


def authenticate(request):
    """
    Authenticate a user
    Args:
        request: 

    Returns:

    """
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


def create_order_for_user(request):
    """
    
    Args:
        request: 

    Returns:

    """
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    city = request.POST.get('city')
    country = request.POST.get('country')
    state = request.POST.get('state')
    pin = request.POST.get('pin')
    user = request.user
    create_order(address, phone, city, country, state, pin, user)
    clear_cart(user)
    return redirect('/')


def add_to_cart(request):
    """
    
    Args:
        request: 

    Returns:

    """
    product_id = request.POST.get("id", "")
    user = request.user
    Cart.objects.create(user=user, product_id=product_id)
    return redirect('/')
