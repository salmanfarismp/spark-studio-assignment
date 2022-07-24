
from django.urls import path
from . import views

urlpatterns = [

    path('POST/authentication/generate_otp',views.generate_otp),
    path('POST/authentication/verify_otp',views.verify_otp),

]