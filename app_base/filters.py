from django_filters import rest_framework as filters
from .models import HomePage, Added, Event, Human

class HomePageFilter(filters.FilterSet):
    class Meta:
        model = HomePage
        fields = {
            'name': ['exact', 'icontains'],
        }

class AddedFilter(filters.FilterSet):
    class Meta:
        model = Added
        fields = {
            'name': ['exact', 'icontains'],
        }

class EventFilter(filters.FilterSet):
    class Meta:
        model = Event
        fields = {
            'name': ['exact', 'icontains'],
        }

class HumanFilter(filters.FilterSet):
    class Meta:
        model = Human
        fields = {
            'first_name': ['exact', 'icontains'],
        }


