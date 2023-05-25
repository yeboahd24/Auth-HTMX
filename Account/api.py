from rest_framework import viewsets, permissions

from Account.serializers import CustomUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserViewSet(viewsets.ModelViewSet):
    """ViewSet for the CustomUser class"""

    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
