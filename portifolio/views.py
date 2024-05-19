# views.py
from rest_framework import viewsets
from rest_framework import generics
from .models import Project, Profile, WhatIDo
from .serializers import ProjectSerializer, ProfileSerializer, WhatIDoSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound

# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class UserProjectsListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound("User not found")
        return Project.objects.filter(user=user)
    
class WhatIDoListView(generics.ListAPIView):
    serializer_class = WhatIDoSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound("User not found")
        return WhatIDo.objects.filter(user=user)
    


class UserProfileDetailView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound("User not found")
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise NotFound("Profile not found")
        return profile
        
    