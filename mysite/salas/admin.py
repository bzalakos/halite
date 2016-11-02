from django.contrib import admin
from .models import Coupon, Product, Purchase, Tag, User

admin.site.register(Coupon)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Tag)
admin.site.register(User)
