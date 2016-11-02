"""Defines the Views. Mostly links templates to object types, some form parsing."""

from django.shortcuts import render
from django.views import generic
from .models import Product, Coupon, Tag, Purchase, User

# Too many anccestors  pylint: disable-msg=R0901
class ProductsListView(generic.ListView):
    """The view of the Products List."""
    context_object_name = 'products_list'
    template_name = 'salas/products.html'
    def get_queryset(self):
        """Gets the list of things to be displayed."""
        return Product.objects.filter()

class ProductView(generic.DetailView):
    """The view of a Product's details."""
    model = Product
    template_name = 'salas/product.html'

class CouponsListView(generic.ListView):
    """The view of the Coupons List."""
    context_object_name = 'coupons_list'
    template_name = 'salas/coupons.html'
    def get_queryset(self):
        """Gets the list of things to be displayed."""
        return Coupon.objects.filter()

class TagsListView(generic.ListView):
    """The view of the Tags List."""
    context_object_name = 'tags_list'
    template_name = 'salas/tags.html'
    def get_queryset(self):
        """Gets the list of things to be displayed."""
        return Tag.objects.filter()

class PurchasesListView(generic.ListView):
    """The view of the Purchases List."""
    context_object_name = 'purchases_list'
    template_name = 'salas/purchases.html'
    def get_queryset(self):
        """Gets the list of things to be displayed."""
        return Purchase.objects.filter()

class PurchaseView(generic.DetailView):
    """The view of a Purchase's details."""
    model = Purchase
    template_name = 'salas/purchase.html'

class AccountView(generic.DetailView):
    """The view of the user's Account page."""
    model = User
    template_name = 'salas/account.html'

class UsersListView(generic.ListView):
    """The view of the Users List."""
    context_object_name = 'users_list'
    template_name = 'salas/users.html'
    def get_queryset(self):
        """Gets the list of things to be displayed."""
        return User.objects.filter()
