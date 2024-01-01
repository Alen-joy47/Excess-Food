import requests
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from ExcessFoodApp.models import Donor, UserRequest
from django.utils import timezone
# from datetime import datetime
from datetime import datetime, timedelta, timezone

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
            user_date = user.date.replace(tzinfo=None)  # Assuming user.date is already an aware datetime
            current_date = current_date.replace(tzinfo=None)

            if user_date > current_date:
                food_name = user.food_name
                donor_queryset = Donor.objects.all()

                # Using list comprehension to create a list of email addresses
                email_list = [donor.email for donor in donor_queryset]
                subject = "Reminder Notification on Excess Food"
                message = message =  f'''This is a friendly reminder that the user request for {food_name} has been noted, and it is scheduled for {user_date}.

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



