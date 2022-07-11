from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from .models import Doctors, Patients
from .serializers import DoctorSerializer, PatientSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          )


class PatientList(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(doctor=self.request.user)


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'doctors': reverse('doctor-list', request=request, format=format),
        'patients': reverse('patient-list', request=request, format=format),
    })

