# myapp/serializers.py
from rest_framework import serializers
from .models import HomePage, Added, Event, Human

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'

class AddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Added
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = '__all__'
