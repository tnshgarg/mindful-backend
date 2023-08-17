from rest_framework import serializers
from .models import User, AppointmentInfo, AppointmentConsent, AppointmentInsuranceInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AppointmentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentInfo
        fields = '__all__'

class AppointmentConsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentConsent
        fields = '__all__'
        
class AppointmentInsuranceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentInsuranceInfo
        fields = '__all__'
