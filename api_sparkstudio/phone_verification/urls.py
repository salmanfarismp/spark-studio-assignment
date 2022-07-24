
from django.urls import path
from . import views

urlpatterns = [

    path('authentication/generate_otp',views.generate_otp),
    path('authentication/verify_otp',views.verify_otp),

]