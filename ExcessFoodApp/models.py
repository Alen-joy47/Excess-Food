from unittest.util import _MAX_LENGTH
from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.


class Donor(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=100, null=False)
    gender = models.IntegerField(null=True)
    address = models.TextField(max_length=200, null=True)
    location = models.TextField(max_length=200, null=True)
    password = models.TextField(max_length=200, null=True)
    is_verified = models.IntegerField(default=0)
    otp = models.CharField(max_length=6, null=True)
    is_enabled = models.IntegerField(default=1)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)

    class Meta:
        db_table = "donors"


class Food(models.Model):
    donor_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(null=True)
    prepared_time = models.DateTimeField(null=True)
    is_deliverable = models.CharField(max_length=100, null=True)
    ingredients = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="food_images/", max_length=250, null=False, default=None)
    is_enabled = models.IntegerField(default=1)
    is_deleted = models.IntegerField(default=0)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        # Convert created_date and updated_date to Indian Standard Time (IST) and add 5 hours and 30 minutes
        if not self.id:
            self.created_date = timezone.now().astimezone(timezone.get_fixed_timezone(330)) + timezone.timedelta(minutes=330)
        self.updated_date = timezone.now().astimezone(timezone.get_fixed_timezone(330)) + timezone.timedelta(minutes=330)
        
        super().save(*args, **kwargs)

    class Meta:
        db_table = "foods"

class User(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=100, null=False)
    gender = models.IntegerField(null=True)
    address = models.TextField(max_length=200, null=True)
    location = models.IntegerField(null=True)
    password = models.TextField(max_length=200, null=True)
    is_verified = models.IntegerField(default=0)
    otp = models.CharField(max_length=6, null=True)
    is_enabled = models.IntegerField(default=1)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)


    class Meta:
        db_table = "users"

class Rating(models.Model):
    order_id = models.IntegerField(null=True)
    food_id = models.IntegerField(null=False)
    donor_id = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)
    ratings = models.IntegerField(null=True)
    description = models.TextField(null=True)
    is_enabled = models.IntegerField(default=1)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)


    class Meta:
        db_table = "ratings"

class Order(models.Model):
    order_id = models.IntegerField(null=True)
    food_id = models.IntegerField(null=False)
    donor_id = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)
    quantity = models.IntegerField(null=True)
    address = models.TextField(null=True)
    description = models.TextField(null=True)
    order_status = models.IntegerField(default=1)
    is_rated = models.IntegerField(default=0)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)


    class Meta:
        db_table = "orders"


class UserRequest(models.Model):

    req_type = models.IntegerField(default=1)
    user_id = models.IntegerField(null=True)
    food_name = models.CharField(max_length=200, null=True)
    food_type = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(null=True)
    quantity = models.IntegerField(null=True)
    description = models.TextField(null=True)
    seen_donor = models.TextField(null=True)
    req_status = models.IntegerField(default=1)
    is_read = models.BooleanField(default=False)  # Track the read status
    image = models.ImageField(upload_to="QR_CODE/" , max_length=250, null=True, default=None)
    is_delivered = models.IntegerField(default=0)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)


    class Meta:
        db_table = "requests"

class Places(models.Model):
    name = models.CharField(max_length=200, null=True)
    values = models.IntegerField(default=1)

    class Meta:
        db_table = "places"