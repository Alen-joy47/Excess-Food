import requests  # type: ignore
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from ExcessFoodApp.models import Donor, UserRequest
from django.utils import timezone
from datetime import datetime, timedelta, timezone
import requests


def send_otp_to_phone(phone):
    try:
        otp = random.randint(111111, 999999)
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/+91{phone}/{otp}/OTP1'
        response = requests.get(url)
        return otp
    except Exception as e:
        return None
    

def send_email(request):
    if request.method == 'GET':
        user_req = UserRequest.objects.filter(req_type = 1).all()
        current_date = datetime.now()

        for user in user_req:
            # print(type(user.date))
            user_date = user.date.replace(tzinfo=None)  # Assuming user.date is already an aware datetime  # type: ignore
            current_date = current_date.replace(tzinfo=None)

            if user_date > current_date:
                food_name = user.food_name
                donor_queryset = Donor.objects.all()

                # Using list comprehension to create a list of email addresses
                email_list = [donor.email for donor in donor_queryset]
                subject = "Reminder Notification on Excess Food"
                message =  f'''This is a friendly reminder that the user request for {food_name} has been noted, and it is scheduled for {user_date}.

We look forward to serving you on {user_date}.

If you have any special preferences or additional requests, feel free to let us know.

For more details please login to your account..

Thanks,
Excess Food Community.'''
                from_email = settings.EMAIL_HOST_USER
                to_email = email_list
                send_mail(subject, message, from_email, to_email)
                print("Email sent successfully...")

    return HttpResponse("hello")


def send_email_new_request(request):
    if request.method == 'POST':
        donor_queryset = Donor.objects.all()

        # Using list comprehension to create a list of email addresses
        email_list = [donor.email for donor in donor_queryset]
        subject = "New Request Notification on Excess Food"
        message = f'''Dear User,

We wanted to inform you that a new request for food/money has been added. 

If you have any special preferences or additional requests, feel free to let us know.

For more details and to manage your requests, please log in to your account on our website.

If you want more details or have any questions, please visit our website.

Thanks for being a part of the Excess Food Community!

Best regards,
Excess Food Community Team
'''
        from_email = settings.EMAIL_HOST_USER
        to_email = email_list
        send_mail(subject, message, from_email, to_email)
        print("Email sent successfully...")

    return HttpResponse("hello")


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return temperature, humidity
    else:
        return None


def send_otp_to_mail(email):
    # Generate a 6-digit OTP
    otp = random.randint(100000, 999999)

    # Using list comprehension to create a list of email addresses
    email_list = [email]
    subject = "Account Activation OTP for Excess Food"
    
    message = f'''Dear User,

Thank you for creating an account on Excess Food. Your OTP for account activation is: {otp}

For more details and to complete the activation process, please log in to your account on our website.

If you have any questions or need assistance, please visit our website.

Thanks for being a part of the Excess Food Community!

Best regards,
Excess Food Community Team
'''
    
    from_email = settings.EMAIL_HOST_USER
    to_email = email_list

    send_mail(subject, message, from_email, to_email)
    print("Activation OTP sent successfully...")

    return otp


