from django.db import models

# Create your models here.

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    large_category = models.CharField(max_length=30)
    specific_category = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    star =
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=700)
    
    def __str__(self):
        return self.name