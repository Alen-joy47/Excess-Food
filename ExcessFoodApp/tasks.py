from ExcessFoodApp.models import *
from django.utils import timezone
from datetime import timedelta

def delete_food_every_day():
    hrs = timezone.now() - timedelta(hours=12)
    foods = Food.objects.filter(created_date__lte=hrs)
    for food in foods:
        food.is_deleted = 1 
        food.save()
    print("Deleted successfully...")

