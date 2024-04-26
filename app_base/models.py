from django.db import models

# Create your models here.

class HomePage(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
    link = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Home'
        db_table = 'homes'
    

class Added(models.Model):
    name = models.CharField(max_length=255)
    add_date = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100)
    export = models.IntegerField()
    income = models.DecimalField(max_digits=20, decimal_places=2)
    company = models.CharField(max_length=50)
    image = models.ImageField(upload_to='added/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Added'
        db_table = 'added'


class Event(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    city = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='events/')
    added = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Events'
        db_table = 'events'


class Human(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    decriptions = models.TextField()
    position = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    image = models.ImageField(upload_to='humans/')

    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = 'Humans'
        db_table = 'humans'
