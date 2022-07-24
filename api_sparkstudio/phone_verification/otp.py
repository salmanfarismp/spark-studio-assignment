import random

def create_otp(request):
    otp = random.randrange(1000,9999)
    return otp