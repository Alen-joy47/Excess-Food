from random import random
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view # type: ignore
from ExcessFoodApp.rawQuery import *
from .helpers import *
from .models import *
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
import random
from django.contrib.auth import logout
from django.views.decorators.cache import cache_control
import requests
from django.utils import timezone
from datetime import datetime
import pytz

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sb
import joblib


utc_now = timezone.now()
ist_now = utc_now.astimezone(timezone.get_fixed_timezone(330))
ist_now_adjusted = ist_now + timedelta(hours=5, minutes=30)
formatted_time = ist_now_adjusted.strftime('%Y-%m-%d %H:%M:%S')


ingredients = ["Eggs", "Milk and milk products", "Fats and oils", "Fruits", "Grain", "Nuts and baking products", "Herbs and spices",
                                    "Pasta", "rice and pulses"]

def indexPage(request):
    foods = Food.objects.filter(is_enabled=1).order_by('-id').all()
    return render(request, "index.html", {"foods" : foods})

def graphs(request):
    return render(request, "graphs.html")

def donorLogin(request):
    if request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']
        donor = Donor.objects.filter(contact = phone, password = password).first()
        if donor != None:
            if donor.is_verified == 1:
                request.session['donorid'] = donor.id # type: ignore
                foods = Food.objects.filter(is_enabled = 1).all()
                id = request.session.get('donorid')
                messages.success(request, "Login Successfully...!")
                return redirect("donorHome")
            else:
                messages.error(request, "Account not found please register now...!")
                return redirect("donorSignup")
        else:
            messages.error(request, "Invalid credentials...!")
            return redirect("donorLogin")
    return render(request, "donor/login.html")

def donorSignup(request):
    locations = Places.objects.all()
    return render(request, "donor/signup.html", {'locations' : locations})

@api_view(['POST'])
def send_otp(request):
    data = request.data
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    gender = data.get('gender')
    address = data.get('address')
    location = data.get('location')
    password = data.get('password')
    repassword = data.get('repassword')
    category = data.get('type')
    if password == repassword:
        if category == "donor":
            donor_phone = Donor.objects.filter(contact = data.get('phone'), email = data.get('email'), is_verified = 1).first()
            if donor_phone != None and donor_phone.contact == data.get('phone') and donor_phone.email == data.get('email') and donor_phone.is_verified == 1:
                messages.error(request, "Duplicate found...")
                return redirect('donorSignup')
            donor_phone1 = Donor.objects.filter(contact = data.get('phone'), email = data.get('email'), is_verified = 0).first()
            if donor_phone1 != None and donor_phone1.contact == data.get('phone') and donor_phone1.email == data.get('email') and donor_phone1.is_verified == 0:
                # otp =send_otp_to_phone(phone)
                otp = 111111
                donor_phone1.name = name
                donor_phone1.gender = gender
                donor_phone1.address = address
                donor_phone1.password = password
                donor_phone1.otp = otp # type: ignore
                donor_phone1.save()
                id = donor_phone1.id # type: ignore
                messages.success(request, 'OTP sent Successfully...!')
                return render(request, "donor/otpVerify.html", {"id" : id, "email" : email})
            if Donor.objects.filter(email=email).exists() or Donor.objects.filter(contact=phone).exists():
                messages.error(request, "Duplicate found....")
                return redirect('donorSignup')  # Redirect to the donor signup page or any other appropriate page
            
            # otp =send_otp_to_phone(phone)
            otp =send_otp_to_mail(email)

            # otp = 111111
            donor = Donor(name = name, contact = phone, email = email, gender = gender, address = address, password = password, otp = otp, created_date = formatted_time)
            donor.save()
            id = donor.id # type: ignore
            phone = donor.contact
            messages.success(request, 'OTP sent Successfully...!')
            return render(request, "donor/otpVerify.html", {"id" : id, "email" : email})
        else:
            donor_phone = User.objects.filter(contact = data.get('phone'), email = data.get('email'), is_verified = 1).first()
            if donor_phone != None and donor_phone.contact == data.get('phone') and donor_phone.email == data.get('email') and donor_phone.is_verified == 1:
                messages.error(request, "Duplicate found...")
                return redirect('userSignup')
            donor_phone1 = User.objects.filter(contact = data.get('phone'), email = data.get('email'), is_verified = 0).first()
            if donor_phone1 != None and donor_phone1.contact == data.get('phone') and donor_phone1.email == data.get('email') and donor_phone1.is_verified == 0:
                # otp =send_otp_to_phone(phone)
                otp =send_otp_to_mail(email)
                # otp = 222222
                donor_phone1.name = name
                donor_phone1.gender = gender
                donor_phone1.address = address
                donor_phone1.location = location
                donor_phone1.password = password
                donor_phone1.otp = otp # type: ignore
                donor_phone1.save()
                id = donor_phone1.id # type: ignore
                messages.success(request, 'OTP sent Successfully...!')
                return render(request, "user/otpVerify.html", {"id" : id, "phone" : phone})
            if User.objects.filter(email=email).exists() or User.objects.filter(contact=phone).exists():
                messages.error(request, "Duplicate found....")
                return redirect('userSignup')  # Redirect to the donor signup page or any other appropriate page
            
            # otp =send_otp_to_phone(phone)
            otp = 222222
            user = User(name = name, contact = phone, email = email, gender = gender, address = address, password = password, location = location, otp = otp, created_date = formatted_time)
            user.save()
            id = user.id # type: ignore
            phone = user.contact
            messages.success(request, 'OTP sent Successfully...!')
            return render(request, "user/otpVerify.html", {"id" : id, "phone" : phone})
    else:
        messages.error(request, "Password does not match...")
        return redirect('index') 
            
@api_view(['POST'])
def verify_otp(request, id):
    data = request.data
    n1 = data.get('num1')
    n2 = data.get('num2')
    n3 = data.get('num3')
    n4 = data.get('num4')
    n5 = data.get('num5')
    n6 = data.get('num6')
    category = data.get('type')
    if category == "donor":
        donors = Donor.objects.get(id=id)
        phone = donors.contact
        otp = f"{n1}{n2}{n3}{n4}{n5}{n6}"
        if donors.otp == otp:
            donors.is_verified = 1
            donors.otp = 0 # type: ignore
            donors.save()
            messages.success(request, "Registration successfully...")
            return redirect("donorLogin")
        else:
            messages.error(request, "Invalid otp")
            return render(request, "donor/otpVerify.html", {"id" : id, "phone" : phone})
    else:
        user = User.objects.get(id=id)
        phone = user.contact
        otp = f"{n1}{n2}{n3}{n4}{n5}{n6}"
        if user.otp == otp:
            user.is_verified = 1
            user.otp = 0 # type: ignore
            user.save()
            messages.success(request, "Registration successfully...")
            return redirect("userLogin")
        else:
            messages.error(request, "Invalid otp")
            return render(request, "user/otpVerify.html", {"id" : id, "phone" : phone})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_all(request):
    # Clear session data
    request.session.flush()
    # Log the user out
    logout(request)
    # Redirect to index page
    response = redirect('index')  

    # Clear session cookies on the client-side
    response.delete_cookie('sessionid')

    messages.success(request, "Logout Successfully...!")
    return response
    # return redirect(reverse('index')) 

def add_food(request, id):
    if id == 0:
        messages.error(request, "Please login before to add food...!")
        return redirect("donorLogin")
    if request.method == "POST" : 
        name = request.POST['name']
        type = request.POST['type']
        category = request.POST['category']
        ingredient = request.POST.getlist('ingredients')
        ingredientss = ', '.join(ingredient[:-1])
        if ingredient:  # Check if the list is not empty
            ingredientss += ingredient[-1]  # Append the last element

        quantity = request.POST['qty']
        preparation_time = request.POST['preparation_time']
        is_del = request.POST.get('is_del', 'No')
        description = request.POST['description']
        print(preparation_time)
        id = request.session['donorid']
        foods = Food(name = name, type = type, ingredients = ingredientss, quantity = quantity, category= category, prepared_time=preparation_time, is_deliverable= is_del,  description = description,  image = request.FILES['images'], donor_id = id, created_date = formatted_time)
        foods.save()
        foods = Food.objects.filter(is_enabled=1).order_by('-id').all()
        messages.success(request, "Food added successfully...!")
        return render(request, "donor/home.html", {"id" : id, "ingredients" : ingredients, "foods" : foods})

    return redirect("index")

def donorHome(request):
    if 'donorid' in request.session:
        id = request.session['donorid']
    else:
        id = 0
    if id == 0:
        return redirect("donorLogin")
    else:
        #Display the list of unread requests
        unread_requests = UserRequest.objects.filter(is_read=False).exclude(seen_donor__contains=str(id))
        
        # Get and reset the unread request count
        count = unread_requests.count()

        foods = Food.objects.filter(is_enabled=1).order_by('-id').all()
        return render(request, "donor/home.html", {"ingredients" : ingredients, "foods" : foods, "id" : id, 'count' : count})

def get_food(request, id, donor_id, category):
    if category == 0:
        food = Food.objects.filter(id = id).first()
        ratings = get_ratings(donor_id)
        if not ratings:
            rating = 0
        else:
            rating = ratings[0]['rating']
        return render(request, "donor/foodDetails.html", {"food" : food, 'rating' : rating})
    else:
        food = Food.objects.filter(id = id).first()
        ratings = get_ratings(donor_id)
        if not ratings:
            rating = 0
        else:
            rating = ratings[0]['rating']

        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': "Mangalore",
            'appid': "8018adbb3f533582a7a5ccc7f533fab3",
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
             # Check if temperature is not None before converting
            if temperature is not None:
                temperature_celsius = kelvin_to_celsius(temperature)
            else:
                temperature_celsius = None
        # temperature_celsius = 30.00
        # humidity = 50
        print("Temp",temperature_celsius)
        print("Temp {:.2f}".format(temperature_celsius))

        return render(request, "user/foodDetails.html", {"food" : food, 'rating' : rating, 'temperature' : temperature_celsius, 'humidity' : humidity})

def kelvin_to_celsius(kelvin_temp):
    celsius_temp = kelvin_temp - 273.15
    return round(celsius_temp, 2)  

def userLogin(request):
    if request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']
        user = User.objects.filter(contact = phone, password = password).first()
        if user != None:
            if user.is_verified == 1:
                request.session['userid'] = user.id # type: ignore
                messages.success(request, "Login Successfully...!")
                return redirect("userHome")
            else:
                messages.error(request, "Please Verify Account...!")
                return redirect("userSignup")
        else:
            messages.error(request, "Invalid credentials...!")
            return redirect("userLogin")
    return render(request, "user/login.html")

def userSignup(request):
    locations = Places.objects.all()
    return render(request, "user/signup.html", {'locations' : locations})

def userHome(request):
    if 'userid' in request.session:
        id = request.session['userid']
    else:
        id = 0
    if id == 0:
        return redirect("userLogin")
    else:
        foods = Food.objects.filter(is_enabled=1).order_by('-id').all()
        return render(request, "user/home.html", {"ingredients" : ingredients, "foods" : foods, "id" : id})

def profile(request, id, category):
    if category == 0:
        donor = Donor.objects.filter(id = id).first()
        return render(request, "donor/profile.html", {"id" : id, "donor" : donor})
    else:
        user = User.objects.filter(id = id).first()
        return render(request, "user/profile.html", {"id" : id, "user" : user})

def ratings(request, category):
    if category == 0:
        # donor = Donor.objects.filter(id = id).first()
        return render(request, "donor/ratings.html")
    else:
        if request.method == 'POST':
            id = request.session['userid']
            order_id = request.POST['order_id']
            ratings = request.POST['ratings']
            description = request.POST['description']

            order= Order.objects.filter(order_id = order_id).first()
            if order != None:
                food_id = int(order.food_id)
                donor_id = int(order.donor_id)

                rating = Rating(food_id = food_id, donor_id = donor_id, user_id = id, ratings = ratings, description = description, order_id = order_id, created_date = formatted_time)
                rating.save()
                orders = Order.objects.filter(order_id = order_id).first()
                if orders != None:
                    orders.is_rated = 1
                    orders.save()
                    foods = Food.objects.filter(is_enabled = 1).order_by('-id').all()
                    messages.success(request, "Rating given success...")
                    return render(request, "user/home.html", {"ingredients" : ingredients, "foods" : foods, "id" : id})

        id = request.session['userid']
        orders = get_Data(id)
        ratings = get_user_ratings(id)
        return render(request, "user/ratings.html", {"orders" : orders, 'ratings' : ratings})
    
def editProfile(request, id, category):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    gender = request.POST['gender']
    address = request.POST['address']
    if category == 0:
        donors = Donor.objects.get(id = id)
        if donors != None : 
            donors.name = name
            donors.contact = phone
            donors.email = email
            donors.gender = gender
            donors.address = address
            donors.updated_date = formatted_time # type: ignore
            donors.save()
            donor_id = donors.id # type: ignore
            messages.success(request, "Profile updated successfully...")
            donor = Donor.objects.filter(id = donor_id).first()
            return render(request, "donor/profile.html", {"donor" : donor})
        else:
            donor_id = donors.id # type: ignore
            messages.success(request, "User not found...")
            donor = Donor.objects.filter(id = donor_id).first()
            return render(request, "donor/profile.html", {"donor" : donor})
    else:
        users = User.objects.get(id = id)
        if users != None : 
            users.name = name
            users.contact = phone
            users.email = email
            users.gender = gender
            users.address = address
            users.updated_date = formatted_time # type: ignore
            users.save()
            user_id = users.id # type: ignore
            messages.success(request, "Profile updated successfully...")
            user = User.objects.filter(id = user_id).first()
            return render(request, "user/profile.html", {"user" : user})
        else:
            user_id = users.id # type: ignore
            messages.success(request, "User not found...")
            user = User.objects.filter(id = user_id).first()
            return render(request, "user/profile.html", {"user" : user})

def view_food(request, id):
    foods = Food.objects.filter(donor_id = id).order_by('-id').all()
    id = request.session['donorid']
    return render(request, "donor/viewFood.html", {"id" : id, "ingredients" : ingredients, "foods" : foods})

def change_food_status(request, id, value) :
    food = Food.objects.get(id = id)
    food.is_enabled = value
    food.save()
    id = food.donor_id
    foods = Food.objects.filter(donor_id = id).order_by('-id').all()
    messages.success(request, "Food status has been updated...!")
    return render(request, "donor/viewFood.html", {"id" : id, "ingredients" : ingredients, "foods" : foods})

def delete_food(request, id):
    food = Food.objects.get(id = id)
    food.delete()
    id = request.session['donorid']
    foods = Food.objects.filter(donor_id = id).order_by('-id').all()
    messages.success(request, "Food has been deleted successfully...!")
    return render(request, "donor/viewFood.html", {"id" : id, "ingredients" : ingredients, "foods" : foods})

def get_food_to_edit(request):
    if request.method == 'GET':
        food_id = request.GET.get('id', None)
        if food_id != None:
            try:
                food = Food.objects.get(id=food_id)
                # Convert food details to a dictionary
                food_details = {
                    'id': food.id, # type: ignore
                    'name': food.name,
                    'type': food.type,
                    'ingredients': food.ingredients,
                    'prepared_time' : food.prepared_time,
                    'is_deliverable' : food.is_deliverable,
                    'quantity': food.quantity,
                    'description': food.description,
                    # 'image': food.image,
                }
                return JsonResponse(food_details, safe=False, encoder=DjangoJSONEncoder)
            except Food.DoesNotExist:
                return JsonResponse({'error': 'Food item not found'}, status=404)
        else:
            return JsonResponse({'error': 'Missing food ID parameter'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
def update_food(request):
    if request.method == "POST" : 
        id = request.POST['id']
        name = request.POST['name']
        type = request.POST['type']
        ingredient = request.POST.getlist('ingredients')
        is_del = request.POST.get('is_del', 'No')
        ingredients = ', '.join(ingredient[:-1])
        if ingredient:  # Check if the list is not empty
            ingredients += ingredient[-1]  # Append the last element

        quantity = request.POST['qty']
        description = request.POST['description']
        food =Food.objects.get(id = id)
        food.name = name
        food.type = type
        food.ingredients = ingredients
        food.quantity = quantity
        food.description = description
        food.is_deliverable = is_del
        food.image = request.FILES['images']
        food.updated_date = formatted_time # type: ignore
        food.save()
        id = request.session['donorid']
        foods = Food.objects.filter(is_enabled = 1).order_by('-id').all()
        messages.success(request, "Food updated successfully...!")
        return render(request, "donor/home.html", {"id" : id, "ingredients" : ingredients, "foods" : foods})
    
def order_food(request):
    if request.method == "POST":
        food_id = request.POST['food_id']
        donor_id = request.POST['donor_id']
        user_id = request.session['userid']
        quantity = int(request.POST['quantity'])
        address = request.POST['address']
        description = request.POST['description']

        order_id = random.randrange(111111, 999999)

        food_qty = Food.objects.filter(id = food_id).first()
        if quantity > int(food_qty.quantity): # type: ignore
            id = request.session['userid']
            foods = Food.objects.filter(is_enabled = 1).order_by('-id').all()
            messages.error(request, "Out of stock... please try again")
            return render(request, "user/home.html", {"ingredients" : ingredients, "foods" : foods, "id" : id})


        order = Order(order_id =order_id, food_id = food_id, donor_id = donor_id, user_id = user_id, quantity = quantity, address = address, description = description, created_date = formatted_time)
        order.save()
        food = Food.objects.get(id = food_id)
        food.quantity -= quantity # type: ignore
        food.save()
        id = request.session['userid']
        foods = Food.objects.filter(is_enabled = 1).order_by('-id').all()
        messages.success(request, "Food ordered successfully...!")
        return render(request, "user/home.html", {"ingredients" : ingredients, "foods" : foods, "id" : id})

def view_history(request):
    id = request.session['userid']
    orders = Order.objects.filter(user_id = id).order_by('-id').all()
    foods = Food.objects.all()
    donors = Donor.objects.all()
    return render(request, "user/orderHistory.html", {"orders" : orders, "foods" : foods, "donors" : donors})

def view_request(request):
    id = request.session['donorid']
    orders = Order.objects.filter(donor_id = id).order_by('-id').all()
    foods = Food.objects.all()
    users = User.objects.all()
    return render(request, "donor/viewRequest.html", {"orders" : orders, "foods" : foods, "users" : users})

def food_request(request, category):
    if category == 1:
        if request.method == 'POST':
            food_name = request.POST['food_name']
            type = request.POST['type']
            user_date = request.POST['req_date']
            qty = request.POST['qty']
            desc = request.POST['description']
            user_id = request.session['userid']

            requests = UserRequest(user_id = user_id, food_name = food_name, food_type = type, date = user_date, quantity = qty, description = desc, created_date = formatted_time)
            requests.save()
            send_email_new_request(request)
            id = request.session['userid']
            foods = Food.objects.filter(is_enabled = 1).order_by('-id').all()
            messages.success(request, "Request send successfully...!")
            return render(request, "user/home.html", {"ingredients" : ingredients, "foods" : foods, "id" : id})
    else:
         if request.method == 'POST':
            user_id = request.session['userid']

            requests = UserRequest(user_id = user_id, image = request.FILES['image'], req_type = 2 , created_date = formatted_time)
            requests.save()
            send_email_new_request(request)
            id = request.session['userid']
            foods = Food.objects.filter(is_enabled = 1).all()
            messages.success(request, "Request send successfully...!")
            return render(request, "user/home.html", {"ingredients" : ingredients, "foods" : foods, "id" : id})
         
def request_list(request):
    foods = get_request_data()
    moneys = get_request_money()
    donor_id = request.session['donorid']

    req_objects = UserRequest.objects.all()
    for req in req_objects:
        # Split the existing seen_donor field into a list of donor IDs
        existing_donor_ids = set(map(int, req.seen_donor.split(','))) if req.seen_donor else set()

        # Add the new donor_id if it's not already present
        if donor_id not in existing_donor_ids:
            existing_donor_ids.add(donor_id)
            # Join the updated set of donor IDs and save the changes
            req.seen_donor = ','.join(map(str, existing_donor_ids))
            req.save()
    return render(request, 'donor/requestList.html', {'foods' : foods, 'moneys' : moneys})

def send_email_to_donor(request):
    send_email(request)
    return redirect('index')

def test_food(request, foodId, temp, humidity):
    # print("Temp",temp)
    # print("Humidity",humidity)
    user_id = request.session['userid']

    user = User.objects.filter(id = user_id).first()
    
    food = Food.objects.filter(id=foodId).first()
    item_id = 0
    is_dairy_product = 0
    food_type = 0
    food_category = food.category
    temp_val = 0
    hum_val = 0
    prepared_value = 0
    food_time = 0
    destination = user.location

    food_name = food.name

    if food_name == "Rice":
        item_id = 1
        food_time = 8
    elif food_name == "Curd Rice":
        item_id = 2
        food_time = 4
    elif food_name == "Biryani":
        item_id = 3
        food_time = 7
    elif food_name == "Chapati":
        item_id = 4
        food_time = 10
    elif food_name == "Paisa":
        item_id = 5
        food_time = 6
    elif food_name == "Samber":
        item_id = 6
        food_time = 10
    elif food_name == "Koorma":
        item_id = 7
        food_time = 8
    elif food_name == "Palya":
        item_id = 8
        food_time = 6
    else:
        item_id = 0
        food_time = 5

    # print("Item id is :", item_id)

    if float(temp) > 35:
        temp_val = 1
    
    if float(humidity) > 80:
        hum_val = 1
    
    if food is not None:
        print("ingredients ",food.ingredients)
        ingredients_string = food.ingredients
        required_ingredients = ["Eggs", "Milk and milk products"]

        for ingredient in required_ingredients:
            if ingredient in ingredients_string:
                is_dairy_product = 1
                # print(f"{ingredient} is present.")
            # else:
                # print(f"{ingredient} is not present.")
        if food.type == "Pure Veg":
            food_type = 0
        else: 
            food_type = 1

        prepared_time = food.prepared_time
        # print(prepared_time)

        current_datetime = datetime.now(prepared_time.tzinfo)

        # print("Original prepared_time:", prepared_time)
        # print("Original current_datetime:", current_datetime)

        # Add 5.5 hours to current_datetime
        current_datetime += timedelta(hours=5, minutes=30)

        # print("Modified current_datetime:", current_datetime)

        # Calculate the time difference
        time_difference = current_datetime - prepared_time

        # Print the time difference
        # print(f"Time difference: {time_difference}")
        # print(f"Time difference: {time_difference}")
        # print(f"Food expairs in  : {food_time} hrs")


        # Check if time difference is greater than 5 hours and days > 1
        if time_difference.total_seconds() > food_time * 3600 or time_difference.days > 1:
            prepared_value = 1
        else:
            prepared_value = 0
        
        print("-"*50)
        print("Temperature :",temp)
        print("Item id is :", item_id)
        print("Dairy ", is_dairy_product)
        print("Type ", food_type)
        # print("category ", food_category)
        print("Time(lifespan) ", prepared_value)
        print("temp ", temp_val)
        # print("humidity ", hum_val)
        print("location(distance) ", destination)
        print("-"*50)

        modal_val = [item_id, is_dairy_product, food_type, prepared_value, temp_val, destination]
        print("-"*50)
        print(modal_val)
        print("-"*50)



        # Specify the correct encoding (e.g., 'ISO-8859-1' or 'utf-16') based on your data
        dataset = pd.read_csv('media/final_food_dataset.csv')

        # Rest of your code remains unchanged
        dataset.shape
        X = np.array(dataset.iloc[:, :-1])
        X = X.astype(dtype='int')
        Y = np.array(dataset.iloc[:, -1])
        Y = Y.reshape(-1,)

        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

        # print(X_train.shape)

        model_food = RandomForestClassifier(n_estimators=100, criterion='entropy')
        model_food.fit(X_train, y_train)
        # X_test = [is_dairy_product, food_type, food_category, prepared_value, temp_val, hum_val, destination]
        X_test = [item_id, is_dairy_product, food_type, prepared_value, temp_val, destination]

        y_predicted = model_food.predict(np.asarray(X_test).reshape(1, -1))
        # print(type(y_predicted[0]))
        result = str(y_predicted[0])
        # print(type(result))
        print(resu)
        id = request.session['userid']
        foods = Food.objects.filter(is_enabled = 1).order_by('-id').all()
        return render(request, "user/home.html", {"ingredients" : ingredients, "foods" : foods, "id" : id, 'result' : result})
    