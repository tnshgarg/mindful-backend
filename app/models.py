from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    dob = models.DateField() # Using DateField for date of birth
    state = models.CharField(max_length=30)
    insurance = models.CharField(max_length=50)
    email = models.EmailField() # Using EmailField for email validation
    password = models.CharField(max_length=128) # Storing password as CharField with limited length

class AppointmentInfo(models.Model):
    appointmentFor= models.CharField(max_length=100, default='Myself')
    gender= models.CharField(max_length=50, default='Male')
    pronouns= models.CharField(max_length=50, default='He/Him')
    servicesInterestedIn= ArrayField( models.CharField(max_length=200), default=list)
    prefferedAppointmentDateAndTime= ArrayField( models.CharField(max_length=200), default=list)
    prefferedVisitType= models.CharField(max_length=50, default="default")
    prefferedProvidedGender= models.CharField(max_length=50, default="default")
    reasonForVisit= models.CharField(max_length=1000, default="default")
    emergencyContactFirstName= models.CharField(max_length=50, default="default")
    emergencyContactLastName= models.CharField(max_length=50, default="default")
    relationshipWithEmergencyContact= models.CharField(max_length=50, default="default")
    emergencyContactPhoneNumber= models.CharField(max_length=50, default="default")

class AppointmentConsent(models.Model):
    acknowledgement1= models.BooleanField(default=False)
    acknowledgement2= models.BooleanField(default=False)
    acknowledgement3= models.BooleanField(default=False)
    acknowledgement4= models.BooleanField(default=False)

class AppointmentInsuranceInfo(models.Model):
    isUsingInsurance= models.BooleanField(default=False)
    isSelfPayPayment= models.CharField(max_length=100, default="default")
    insuranceCompany= models.CharField(max_length=400, default="default")
    subscriberMemberId= models.CharField(max_length=200, default="default")
    frontImage = models.FileField(upload_to='insurance_docs/', null=True, blank=True) 
    backImage = models.FileField(upload_to='insurance_docs/', null=True, blank=True)