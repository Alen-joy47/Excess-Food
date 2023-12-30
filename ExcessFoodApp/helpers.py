# import requests
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from ExcessFoodApp.models import Donor, UserRequest
from django.utils import timezone
# from datetime import datetime
from datetime import datetime, timedelta, timezone


# utc_now = timezone.now()

# # Convert UTC time to Indian Standard Time (IST)
# ist_now = utc_now.astimezone(timezone.get_fixed_timezone(330))  # UTC+5:30 for Indian Standard Time

# # Format the datetime as a string if needed
# formatted_time = ist_now.strftime('%Y-%m-%d %H:%M:%S')

def send_otp_to_phone(phone):
    try:
        otp = random.randint(111111, 999999)
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/+91{phone}/{otp}/OTP1'
        # response = requests.get(url)
        return otp
    except Exception as e:
        return None
    

def send_email(request):
    if request.method == 'GET':
        user_req = UserRequest.objects.all()
        if user_req is not None:
            for user in user_req:
                # date1 = user.date
                # date2 =  datetime.now()
                # print(user.date)

                # temp_date = user.date
                print("user-data:- ",user.date)
                print(type(user.date))

                current_date = datetime.now()
                print("user-current_date:- ",current_date)
                print(type(current_date))

                # Assuming your datetime object is named 'your_datetime_object'
                # your_datetime_object = datetime(2024, 1, 4, 15, 1, tzinfo=timezone.utc)

                # Convert to a specific timezone if needed (e.g., 'Asia/Kolkata')
                temp =user.date
                # local_timezone = timezone(timedelta(hours=5, minutes=30))  # UTC+5:30 for 'Asia/Kolkata'
                # your_datetime_object_local = temp.astimezone(local_timezone)

                # # Extract the date
                # date_only = your_datetime_object_local.date()
                # date_only = datetime.strptime(str(temp), "%Y-%m-%d")
                # formatted_date = datetime.strptime(str(temp), "%Y-%m-%d %H:%M:%S.%f")
                # print("temp formatted_date:- ",temp.date())
                # print(type(temp.date()))
                # if temp > current_date:

    return HttpResponse("hello")



       
        # # print(date_time_obj)


        # # Convert to string with a specific format
        # # date_str1 = obj_date_time.strftime('%Y-%m-%d')
        # current_date = datetime.strptime(str(date_time_obj),'%Y-%m-%d')
        
        # # Convert string dates to datetime objects
        # # date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        # userDate = datetime.strptime(str(temp_date), "%Y-%m-%d")
        
        # # Compare the dates
        # if userDate > current_date:
        #     food_date = user.date
        #     food_name = user.food_name
        #     donor_queryset = Donor.objects.all()

        #     # Using list comprehension to create a list of email addresses
        #     email_list = [donor.email for donor in donor_queryset]
        #     subject = "Reminder Notification on Excess Food"
        #     message = f'''
        #                 This is a friendly reminder that your request for {food_name} has been noted, and it is scheduled for {food_date}. 
        #                 We look forward to serving you on {food_date}. 
        #                 If you have any special preferences or additional requests, feel free to let us know.
        #                 For more details please check your account.
        #             '''
        #     from_email = settings.EMAIL_HOST_USER
        #     to_email = email_list
        #     send_mail(subject, message, from_email, to_email)
        #     print("Email sent...")
        #     return
