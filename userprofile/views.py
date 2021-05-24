from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from userprofile.serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from userprofile.models import Profile


class UserProfileView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.request.query_params.get('id', None)
        queryset = User.objects.filter(pk=user)
        return queryset
