# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import   UserProfileDetailView, UserProjectsListView, WhatIDoListView

# router = DefaultRouter()
# router.register(r'projects', ProjectViewSet)
# router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    
    path('user/<int:user_id>/projects/', UserProjectsListView.as_view(), name='user-projects'),
    path('user/<int:user_id>/profile/', UserProfileDetailView.as_view(), name='user-profile'),
    path('user/<int:user_id>/what-i-do/', WhatIDoListView.as_view(), name='what-i-do'),
]
