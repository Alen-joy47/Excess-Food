from email import message
from email.mime import image
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import send_otp_to_phone
from .models import *
from django.contrib import messages

utc_now = timezone.now()

# Convert UTC time to Indian Standard Time (IST)
ist_now = utc_now.astimezone(timezone.get_fixed_timezone(330))  # UTC+5:30 for Indian Standard Time

# Format the datetime as a string if needed
formatted_time = ist_now.strftime('%Y-%m-%d %H:%M:%S')

ingredients = ["Eggs", "Milk and milk products", "Fats and oils", "Fruits", "Grain", "Nuts and baking products", "Herbs and spices",
                                    "Meat", "Sausages and fish", "Pasta, rice and pulses"]


def indexPage(request):
    foods = Food.objects.filter(is_enabled = 1).all()
    return render(request, "index.html", {"foods" : foods})

def donorLogin(request):
    if request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']
        donor = Donor.objects.filter(contact = phone, password = password).first()
        if donor != None:
            if donor.is_verified == 1:
                request.session['donorid'] = donor.id # type: ignore
                foods = Food.objects.filter(is_enabled = 1).all()
                messages.success(request, "Login Successfully...!")
                return render(request, "donor/home.html", {"ingredients" : ingredients, "foods" : foods})
            else:
                donor_id = donor.id # type: ignore
                donors = Donor.objects.get(id = donor_id)
                donors.delete()
                messages.error(request, "Account not found please register now...!")
                return redirect("donorSignup")
        else:
            messages.error(request, "Invalid credentials...!")
            return redirect("donorLogin")
    return render(request, "donor/login.html")

def donorSignup(request):
    return render(request, "donor/signup.html")

@api_view(['POST'])
def send_otp(request):
    data = request.data
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    gender = data.get('gender')
    address = data.get('address')
    password = data.get('password')
    category = data.get('type')
    if category == "donor":
        donor_phone = Donor.objects.filter(contact = data.get('phone')).first()
        if donor_phone != None and donor_phone.contact == data.get('phone'):
            messages.error(request, "Duplicate Contact Number")
            return redirect('donorSignup')
        
        donor_email = Donor.objects.filter(email = data.get('email')).first()
        if donor_email != None and donor_email.email == data.get('email'):
            messages.error(request, "Duplicate Email")
            return redirect('donorSignup')
        
        # otp =send_otp_to_phone(phone)
        otp = 123456
        donor = Donor(name = name, contact = phone, email = email, gender = gender, address = address, password = password, otp = otp, created_date = formatted_time)
        donor.save()
        id = donor.id # type: ignore
        phone = donor.contact
        messages.success(request, 'OTP sent Successfully...!')
        return render(request, "donor/otpVerify.html", {"id" : id, "phone" : phone})
    else:
        user_phone = User.objects.filter(contact = data.get('phone')).first()
        if user_phone != None and user_phone.contact == data.get('phone'):
            messages.error(request, "Duplicate Contact Number")
            return redirect('userSignup')
        
        user_email = User.objects.filter(email = data.get('email')).first()
        if user_email != None and user_email.email == data.get('email'):
            messages.error(request, "Duplicate Email")
            return redirect('userSignup')
        
        # otp =send_otp_to_phone(phone)
        otp = 654321
        user = User(name = name, contact = phone, email = email, gender = gender, address = address, password = password, otp = otp, created_date = formatted_time)
        user.save()
        id = user.id # type: ignore
        phone = user.contact
        messages.success(request, 'OTP sent Successfully...!')
        return render(request, "user/otpVerify.html", {"id" : id, "phone" : phone})
    
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

def logout_all(request):
    messages.success(request, "Logout Successfully...!")
    return redirect("index")

def add_food(request, id):
    if id == 0:
        messages.error(request, "Please login before to add food...!")
        return redirect("donorLogin")
    if request.method == "POST" : 
        name = request.POST['name']
        type = request.POST['type']
        ingredient = request.POST.getlist('ingredients')
        ingredients = ', '.join(ingredient[:-1])
        if ingredient:  # Check if the list is not empty
            ingredients += ingredient[-1]  # Append the last element

        description = request.POST['description']

        food = Food.objects.filter(name = name).first()
        if food == None:
            id = request.session['donorid']
            foods = Food(name = name, type = type, ingredients = ingredients, description = description, image = request.FILES['images'], donor_id = id, created_date = formatted_time)
            foods.save()
            donor_id = id
            foods = Food.objects.filter(is_enabled = 1).all()
            messages.success(request, "Food added successfully...!")
            return render(request, "donor/home.html", {"donor_id" : donor_id, "ingredients" : ingredients, "foods" : foods})
        else:
            messages.error(request, "Duplicate food name...!")
            return redirect("donorHome")

    return redirect("index")

def donorHome(request):
    foods = Food.objects.filter(is_enabled = 1).all()
    return render(request, "donor/home.html", {"ingredients" : ingredients, "foods" : foods})

def get_food(request, id, category):
    if category == 0:
        food = Food.objects.filter(id = id).first()
        return render(request, "donor/foodDetails.html", {"food" : food})
    else:
        food = Food.objects.filter(id = id).first()
        return render(request, "user/foodDetails.html", {"food" : food})
   

def userLogin(request):
    if request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']
        user = User.objects.filter(contact = phone, password = password).first()
        if user != None:
            if user.is_verified == 1:
                request.session['userid'] = user.id # type: ignore
                foods = Food.objects.filter(is_enabled = 1).all()
                messages.success(request, "Login Successfully...!")
                return render(request, "user/home.html", {"ingredients" : ingredients, "foods" : foods})
            else:
                user_id = user.id # type: ignore
                users = User.objects.get(id = user_id)
                users.delete()
                messages.error(request, "Account not found please register now...!")
                return redirect("userSignup")
        else:
            messages.error(request, "Invalid credentials...!")
            return redirect("userLogin")
    return render(request, "user/login.html")

def userSignup(request):
    return render(request, "user/signup.html")

def userHome(request):
    foods = Food.objects.filter(is_enabled = 1).all()
    return render(request, "user/home.html", {"ingredients" : ingredients, "foods" : foods})


def profile(request, id, category):
    if category == 0:
        donor = Donor.objects.filter(id = id).first()
        return render(request, "donor/profile.html", {"donor" : donor})
    else:
        user = User.objects.filter(id = id).first()
        return render(request, "user/profile.html", {"user" : user})

def ratings(request, id, category):
    if category == 0:
        donor = Donor.objects.filter(id = id).first()
        return render(request, "donor/ratings.html", {"donor" : donor})
    else:
        user = User.objects.filter(id = id).first()
        return render(request, "user/ratings.html", {"user" : user})
