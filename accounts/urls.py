from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import CustomerUpdateView, CustomerView, EmployeeView, LoginView



urlpatterns = [
    path('employee/create',EmployeeView.as_view()),
    path('customer/create',CustomerView.as_view()),
    path('customer/update/<pk>',CustomerUpdateView.as_view()),
    path('login',LoginView.as_view()),
    path('refresh',TokenRefreshView.as_view())
]