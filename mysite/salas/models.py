"""Defines the models used in the application. Object types, relations."""

from django.db import models

class User(models.Model):
    """A User of the site. Either a Customer or a Distributor."""
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    email_public = models.BooleanField()
    given_name = models.CharField(max_length=50)
    given_name_visible = models.BooleanField()
    family_name = models.CharField(max_length=50)
    family_name_visible = models.BooleanField()
    phone_number = models.CharField(max_length=50)
    phone_number_public = models.BooleanField()
    language = models.CharField(max_length=50)
    # Distributor stuff.
    is_dist = models.BooleanField()
    payment_instructions = models.CharField(max_length=50)
    new_period = models.DurationField()
    sale_id_prefix = models.CharField(max_length=50)
    #Customer stuff.
    address = models.CharField(max_length=50)
    distributor = models.ForeignKey('self', on_delete=models.CASCADE)

class Product(models.Model):
    """A Product for sale. Owned by a User(D)."""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    price = models.FloatField()
    picture_format = models.CharField(max_length=50)
    available = models.BooleanField()
    # Turns out he didn't want all these.
    # begin_date = models.DateTimeField()
    # end_date = models.DateTimeField()
    # quantity = models.IntegerField()
    featured = models.BooleanField
    uploaded = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()

    distributor = models.ForeignKey(User, on_delete=models.CASCADE)

class Coupon(models.Model):
    """A Coupon offering some discount on an order. Owned by a User(D)."""
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    discount = models.FloatField()
    # Might not want these two either then?
    # begin_date = models.DateTimeField()
    # end_date = models.DateTimeField()
    available = models.BooleanField()
    deleted = models.BooleanField()

    distributor = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
    """A Tag marking categories. Owned by a User(D), can be attached to many Products."""
    name = models.CharField(max_length=50)
    deleted = models.BooleanField()

    distributor = models.ForeignKey(User, on_delete=models.CASCADE)

class Purchase(models.Model):
    """A Purchase Receipt, a record of a sale.
    Attached to one User(C) and one User(D), may have a coupon, has one or more Products."""
    total_gross = models.FloatField()
    total_net = models.FloatField()
    sale_date = models.DateTimeField()
    details = models.TextField()
    deleted = models.BooleanField()
    comments = models.CharField(max_length=4000)
    completed = models.BooleanField()
    personal_id = models.PositiveIntegerField()

    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    distributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales')
    products = models.ManyToManyField(Product)
