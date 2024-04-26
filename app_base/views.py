# myapp/views.py
from rest_framework import viewsets
from .models import HomePage, Added, Event, Human
from .serializers import HomePageSerializer, AddedSerializer, EventSerializer, HumanSerializer

class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer

class AddedViewSet(viewsets.ModelViewSet):
    queryset = Added.objects.all()
    serializer_class = AddedSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class HumanViewSet(viewsets.ModelViewSet):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
