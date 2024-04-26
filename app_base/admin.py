from django.contrib import admin
from .models import HomePage, Added, Event, Human

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'image', 'link')

@admin.register(Added)
class AddedAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_date', 'city', 'export', 'income', 'company', 'image')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'city', 'date', 'image', 'added')

@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'decriptions', 'position', 'contact', 'image')
