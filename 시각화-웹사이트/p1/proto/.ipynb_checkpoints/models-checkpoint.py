from django.db import models

# Create your models here.

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    large_category = models.(max_length=30)
    specific_category = models.(max_length=30)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    large_category = models.(max_length=30)
    specific_category = models.(max_length=30)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name