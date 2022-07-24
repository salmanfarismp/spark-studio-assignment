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
    if request.session.get('attempt_failed_date') :
        if request.session['attempt_failed_date'] == str(datetime.date.today()):
            return 0
        else:
            del request.session['attempt_failed_date'] 
    if request.session.get('request_count') and request.session['request_count'] < 10: 
        request_count = request.session.get('request_count')
        request_count = int(request_count) + 1
    else :
        request_count = 1 # if it is a new user or a user that has more than 10 failed attempts on another day.
    request.session['request_count'] = request_count
    if request_count >= 10 :
        request.session['attempt_failed_date'] = str(datetime.date.today())
    return 1



@api_view(['GET'])
def generate_otp(request):
    # valid_attempt = check_user_attempt(request)
    valid_attempt = True
    if valid_attempt:
        otp = create_otp()
        request.session['otp'] = otp
        request.session['otp_generated_time'] = str(datetime.datetime.now())
        print("OTP is :",otp) # As instructed otp is just printing on console
        # send otp in sms using twilio
        return Response('success',status=status.HTTP_200_OK)
    return Response('You have exceeded the limit of verification attempts.You can try again Tommorrow',status=status.HTTP_400_BAD_REQUEST)


def check_otp_expired(request):
    otp_generated_time = request.session.get('otp_generated_time')
    data = otp_generated_time.split(' ')
    date_from_data = data[0].split('-')
    time_from_data = data[1].split(':')
    year = int(date_from_data[0])
    month = int(date_from_data[1])
    day = int(date_from_data[2])
    hour = int(time_from_data[0])
    minute = int(time_from_data[1])
    second = int(float(time_from_data[2]))
    time_that_otp_created =  datetime.datetime(year, month, day, hour, minute, second)
    current_time = datetime.datetime.now()
    print('current time:', current_time)
    checking_time = current_time -  datetime.timedelta(minutes = 30)
    print('checking_time',checking_time, 'time_that_otp_created', time_that_otp_created)
    if time_that_otp_created > checking_time :
        return True
    else :
        return False

    
   


@api_view(['GET'])
def verify_otp(request):
    if request.session.get('otp_generated_time'):
        valid_otp = check_otp_expired(request)
        print(valid_otp)
        # phone = request.data['phone']
        # user_otp = request.data['otp']
        # created_otp = request.session.get('otp')
        return Response('success',status=status.HTTP_200_OK)
    else:
        return Response('Page Not Found',status=status.HTTP_404_NOT_FOUND)
    

    
    


    