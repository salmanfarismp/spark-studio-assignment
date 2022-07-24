from datetime import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view ,permission_classes
import datetime
import json
from .otp import create_otp

# Create your views here.

def check_user_attempt(request):
    if request.session['attempt_failed_date'] == str(datetime.date.today()):
        return 0
    if request.session.get('request_count') and request.session['request_count'] < 10:
        request_count = request.session.get('request_count')
        request_count = int(request_count) + 1
    else :
        request_count = 1
    request.session['request_count'] = request_count
    if request_count >= 10 :
        request.session['attempt_failed_date'] = str(datetime.date.today())
    return 1







@api_view(['GET'])
def generate_otp(request):
    valid_attempt = check_user_attempt(request)
    if valid_attempt:
        otp = create_otp()
        print("OTP is :",otp)
        return Response('success',status=status.HTTP_200_OK)
    return Response('You have exceeded the limit of verification attempts.You can try again Tommorrow',status=status.HTTP_400_BAD_REQUEST)



    
    

    


def check_otp_expired(request):
    return Response('success',status=status.HTTP_200_OK)
    

@api_view(['POST'])
def verify_otp(request):
    pass