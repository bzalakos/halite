"""Defines the models used in the application. Object types, relations."""
# import datetime
from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone

class Profile(models.Model):
    """Holds more information that isn't included in the default User model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_public = models.BooleanField()
    given_name_visible = models.BooleanField()
    family_name_visible = models.BooleanField()
    phone_number = models.CharField(max_length=50)
    phone_number_public = models.BooleanField()
    language = models.CharField(max_length=50)
    # Distributor stuff.
    payment_instructions = models.CharField(max_length=50, blank=True)
    new_period = models.DurationField(blank=True)
    sale_id_prefix = models.CharField(max_length=50, blank=True)
    #Customer stuff.
    address = models.CharField(max_length=50, blank=True)
    distributor = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

class Tag(models.Model):
    """A Tag marking categories. Owned by a User(D), can be attached to many Products."""
    name = models.CharField(max_length=50)
    deleted = models.BooleanField()

    distributor = models.ForeignKey(User, on_delete=models.CASCADE)

class Product(models.Model):
    """A Product for sale. Owned by a User(D), can have many Tags."""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    price = models.FloatField()
    picture = models.ImageField(blank=True)
    # Turns out he didn't want all these.
    # begin_date = models.DateTimeField(null=True)
    # end_date = models.DateTimeField(null=True)
    # quantity = models.IntegerField(null=True)
    enabled = models.BooleanField()
    featured = models.BooleanField()
    uploaded = models.DateTimeField()
    deleted = models.BooleanField()

    distributor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    # def available(self):
    # """Shortcut. This determines whether a Product is available to customers."""
    #     now = timezone.now()
    #     return not self.deleted and (self.begin_date is None or self.begin_date <= now) and (
    #         self.end_date is None or now <= self.end_date) and (
    #         self.quantity is None or self.quantity < 0)
    def available(self):
        """Shortcut. This determines whether a Product is available to customers."""
        return self.enabled and not self.deleted

class Coupon(models.Model):
    """A Coupon offering some discount on an order. Owned by a User(D)."""
    code = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    discount = models.FloatField()
    # Might not want these two either then?
    # begin_date = models.DateTimeField(null=True)
    # end_date = models.DateTimeField(null=True)
    enabled = models.BooleanField()
    deleted = models.BooleanField()

    distributor = models.ForeignKey(User, on_delete=models.CASCADE)

    # def available(self):
    #     """Shortcut. This determines whether a Coupon is available to customers."""
    #     now = timezone.now()
    #     return not self.deleted and (self.begin_date is None or self.begin_date <= now) and (
    #         self.end_date is None or now <= self.end_date)
    def available(self):
        """Shortcut. This determines whether a Coupon is available to customers."""
        return self.enabled and not self.deleted

class Purchase(models.Model):
    """A Purchase Receipt, a record of a sale.
    Attached to one User(C) and one User(D), may have a coupon, has one or more Products."""
    total_gross = models.FloatField()
    total_net = models.FloatField()
    sale_date = models.DateTimeField()
    details = models.TextField()
    comments = models.CharField(max_length=4000)
    completed = models.BooleanField()
    personal_id = models.PositiveIntegerField()

    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    distributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sales')
    products = models.ManyToManyField(Product)
