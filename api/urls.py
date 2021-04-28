from django.urls import path, include, re_path
from .views import UserList, UserDetail

# dj rest auth with jwt
# from dj_rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
#                                 PasswordResetConfirmView, PasswordResetView,
#                                 UserDetailsView)
# from rest_framework_simplejwt.views import TokenVerifyView
# from django.views.generic import TemplateView
app_name = "api"


urlpatterns = [
    # Users
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
]
