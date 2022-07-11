from django.db import models


class Doctors(models.Model):
    joined = models.DateTimeField(auto_now_add=True)
    doc_name = models.CharField(max_length=200, blank=True, default='')
    sector = models.CharField(max_length=200, blank=True, default='Physiothrapist')
    is_available = models.BooleanField(default=True)
    doc_notice = models.TextField()

    class Meta:
        ordering = ['joined']

    def __str__(self):
        return self.doc_name


class Patients(models.Model):
    appointment_date = models.DateTimeField(auto_now_add=True)
    patient_name = models.CharField(max_length=200, blank=True, default='')
    patient_typ = models.CharField(max_length=100, blank=True, default='')
    doctor = models.ForeignKey('auth.User', related_name='doctors', on_delete=models.CASCADE)

    class Meta:
        ordering = ['appointment_date']

    def __str__(self):
        return self.patient_name


