from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .cart import Cart
import midtransclient
import uuid

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 
   

# Create your views here.
@login_required
def home(request):
    filter = request.GET.get("category")

    if filter == "" or filter == None:
        products = Product.objects.all()

    elif filter == "All":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__contains=filter)


    return render(request, 'pages/index.html', {'products': products})


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'pages/productdetail.html', {'p': product})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("index")  # Redirect to homepage after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "pages/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout

def user_register(request):
    form = RegisterForm(data=request.POST)

    if form.is_valid():
        form.save()
        return redirect("login")

    return render(request, "pages/register.html", {"form":form})


def product_list(request):
    category = request.GET.get('category', 'All')
    if category == 'All':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=category)

    return render(request, 'shop/product_list.html', {'products': products, 'selected_category': category})


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart_detail')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'pages/cart_detail.html', {'cart': cart})
   
def checkout(request,item):
    cart = Product.objects.get(id=item)
    order_id = f"ORD-{uuid.uuid4().hex[:10].upper()}"

    param = {
    "transaction_details": {
        "order_id": order_id,
        "gross_amount": int(cart.price)
    }, 
    "credit_card":{
        "secure" : True
        }
    }
    snap = midtransclient.Snap(
    is_production=False,
    server_key='SB-Mid-server-tGHmD0GDxzTq_r78CPIBBz2U',
    client_key='SB-Mid-client-2aXSlzE5ozSTgchV'
)
    transaction = snap.create_transaction_token(param)
    return render(request, 'pages/checkout.html',{"item":item, "token":transaction, "client":"SB-Mid-client-2aXSlzE5ozSTgchV"} )

def history(request):
    transaksi = Transaction.objects.all()
    return render(request, 'pages/history.html')
 

def success(request):
    return render(request, "pages/")