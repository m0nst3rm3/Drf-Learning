from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from serializertutorial import views


urlpatterns = [
    path('doctors/', views.DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view()),
    path('patients/', views.PatientList.as_view(), name='patient-list'),
    path('patients/<int:pk>/', views.PatientDetail.as_view()),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.api_root),
]


urlpatterns = format_suffix_patterns(urlpatterns)
