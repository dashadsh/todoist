# todo/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet, index

router = DefaultRouter()
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    path('', index),
    path('api/', include(router.urls)),
]
