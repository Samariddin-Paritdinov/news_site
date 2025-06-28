from django.urls import path
from accounts.api_endpoints.Profile import (
    ProfileDeleteAPIView,
    ProfileUpdateAPIView,
    PasswordResetRequestAPIView,
    PasswordResetConfirmAPIView,
    RegisterUserAPIView,
    RegisterConfirmAPIView,
)


app_name = 'profile'

urlpatterns = [
    path('profile/delete/', ProfileDeleteAPIView.as_view(), name="profile-delete"),
    path('profile/update/', ProfileUpdateAPIView.as_view(), name="profile-update"),
    path('password-reset/request/', PasswordResetRequestAPIView.as_view(), name="password-reset-request"),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
    path('register/request/', RegisterUserAPIView.as_view(), name="register-request"),
    path('register/confirm/', RegisterConfirmAPIView.as_view(), name="register-confirm"),

]
