import random
from twilio.rest import Client 
from decouple import config

def create_otp():
    otp = random.randrange(1000,9999)
    return otp

def send_otp(request,otp,phone_number):
    account_sid = config('account_sid') 
    auth_token = config('auth_token')
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create(  
                                messaging_service_sid=config('services'), 
                                body=otp,      
                                to=phone_number 
                            ) 
    
    print(message.sid)
    return message.status


    