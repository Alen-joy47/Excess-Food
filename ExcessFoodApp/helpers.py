import requests
import random
from django.conf import settings

def send_otp_to_phone(phone):
    try:
        otp = random.randint(111111, 999999)
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/+91{phone}/{otp}/OTP1'
        response = requests.get(url)
        return otp
    except Exception as e:
        return None