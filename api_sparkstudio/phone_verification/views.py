from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def generate_otp(request):
    if request.session.get('request_count'):
        request_count = request.session.get('request_count')
        request_count = int(request_count) + 1
    else :
        request_count = 0
    request.session['request_count'] = request_count
    if request_count > 10 :
        return Response('You have exceeded the limit of verification attempts',status=status.HTTP_400_BAD_REQUEST)
    else :
        return Response('success',status=status.HTTP_200_OK)
    

def verify_otp(request):
    pass