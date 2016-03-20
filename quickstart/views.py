from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer,LoginSerializer
from quickstart.models import Login

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
class LoginViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Login to be viewed or edited.
    """
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
