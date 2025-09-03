from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import index
urlpatterns = [
    path('', index),
    path('auth/register/', views.RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('patients/', views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),

    path('doctors/', views.DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor-detail'),

    path('mappings/', views.PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', views.PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
]
