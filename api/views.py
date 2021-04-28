from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsSuperUserOrStaffReadOnly
from .serializers import UserSerializer


class UserList(ListCreateAPIView):
    """
    This class show the list of users.
    params ->
        queryset -> list of all users
        serializer_class
        permission_classes -> only superusers can edit the users, staff users can only read
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    """
    This class show a user base on primary key.
    params ->
        queryset -> list of all users
        serializer_class
        permission_classes -> only superusers can edit the user, staff users can only read
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)
