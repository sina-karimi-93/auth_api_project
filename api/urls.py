from django.urls import path, include
from .views import UserList, UserDetail

# dj rest auth with jwt
from dj_rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
                                PasswordResetConfirmView, PasswordResetView,
                                UserDetailsView)
from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view

app_name = "api"

"""
- For access each view that has permission you should insert the access token
in the header, the key is not Token like others, but it is 'Bearer'.
for example -> Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1Ni...

- Every access token has limitation about 5 minutes,after that it will expired.So
you should get new access token by refresh token wich you earlier get for your
credential, in this path: 
    api/accounts/token/refresh/
"""
urlpatterns = [
    # Users
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
    # path('accounts/', include('dj_rest_auth.urls')),

    # Auth
    path('accounts/login/', LoginView.as_view(), name='rest_login'),
    path('accounts/logout/', LogoutView.as_view(), name='rest_logout'),
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
    path('accounts/user/', UserDetailsView.as_view(), name='rest_user_details'),
    # Password
    path('accounts/password/reset/', PasswordResetView.as_view(),
         name='rest_password_reset'),
    path('accounts/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password/change/', PasswordChangeView.as_view(),
         name='rest_password_change'),
    # Token
    path('accounts/token/refresh/',
         get_refresh_view().as_view(), name='token_refresh'),
    path('accounts/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
