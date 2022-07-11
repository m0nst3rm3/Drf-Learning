from rest_framework import serializers
from .models import Doctors, Patients
from django.contrib.auth.models import User

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctors
        fields = ('id', 'joined', 'doc_name', 'sector', 'is_available', 'doc_notice',)


class PatientSerializer(serializers.ModelSerializer):
    doctor = serializers.ReadOnlyField(source='doctor.username')

    class Meta:
        model = Patients
        fields = ('id', 'appointment_date', 'patient_name', 'patient_typ', 'doctor')


class UserSerializer(serializers.ModelSerializer):
    doctors = serializers.PrimaryKeyRelatedField(many=True, queryset=Patients.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'doctors')

