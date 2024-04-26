# myproject/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import HomePageViewSet, AddedViewSet, EventViewSet, HumanViewSet

router = routers.DefaultRouter()
router.register(r'homepages', HomePageViewSet)
router.register(r'addeds', AddedViewSet)
router.register(r'events', EventViewSet)
router.register(r'humans', HumanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
