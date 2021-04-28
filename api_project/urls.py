"""api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from dj_rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
                                PasswordResetConfirmView, PasswordResetView,
                                UserDetailsView)
from dj_rest_auth.jwt_auth import get_refresh_view
from rest_framework_simplejwt.views import TokenVerifyView

"""
====================================== API AUTHENTICATION =======================================
- For access each view that has permission you should insert the access token
in the header, the key is not Token like others, but it is 'Bearer'.
for example -> Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1Ni...

- Every access token has limitation about 5 minutes,after that it will expired.So
you should get new access token by refresh token wich you earlier get for your
credential, in this path: 
    api/accounts/token/refresh/
====================================== API AUTHENTICATION =======================================
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    #  ================================ API AUTHECTICATION ======================================
    path('api/accounts/', include('dj_rest_auth.urls')),
    # Auth
    path('api/accounts/login/', LoginView.as_view(), name='rest_login'),
    path('api/accounts/logout/', LogoutView.as_view(), name='rest_logout'),
    path('api/accounts/register/', include('dj_rest_auth.registration.urls')),
    path('api/accounts/user/', UserDetailsView.as_view(), name='rest_user_details'),
    # Password
    path('api/accounts/password/reset/', PasswordResetView.as_view(),
         name='rest_password_reset'),
    path('api/accounts/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/accounts/password/change/', PasswordChangeView.as_view(),
         name='rest_password_change'),
    # Token
    path('api/accounts/token/refresh/',
         get_refresh_view().as_view(), name='token_refresh'),
    path('api/accounts/token/verify/',
         TokenVerifyView.as_view(), name='token_verify'),
    #  ================================ API AUTHECTICATION ======================================
]
