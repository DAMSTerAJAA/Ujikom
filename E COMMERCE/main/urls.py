from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name="index"),#Home Page
    path('accounts/login/', user_login, name='login'),  # Login page
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # Logout
    path('accounts/register/', user_register, name='regist'),
    path('products/', product_list, name='product_list'),
    path("product/<slug:slug>/",product_detail, name="detail"),
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('checkout/<int:item>', checkout, name="checkout"),
    path('history/', history, name='history'),
]

