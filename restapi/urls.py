from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'user', UserViewSet)

urlpatterns=[
    path('',include(router.urls))
]