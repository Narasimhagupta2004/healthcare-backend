from rest_framework import generics, permissions
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    RegisterSerializer, PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer
)
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse
# Authentication
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Patients
class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

# Doctors
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Patient-Doctor Mapping
class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientDoctorMappingDetailView(generics.RetrieveDestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    return HttpResponse("Hello, world. You're at the healthcare index.")