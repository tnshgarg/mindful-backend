from django.urls import path
from .views import create_user, appointment_info, appointment_consent, appointment_insurance_info

urlpatterns = [
    path('register/', create_user, name='register'),
    path('appointment-info/', appointment_info, name='appointment_info'),
    path('appointment-consent/', appointment_consent, name='appointment_consent'),
    path('insurance-info/', appointment_insurance_info, name='appointment_insurance_info'),
]