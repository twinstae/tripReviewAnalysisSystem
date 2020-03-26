from django.db import models

# Create your models here.

class Attraction(models.Model):
    name = models.CharField(max_length=100)
    large_category = models.CharField(max_length=30)
    specific_category = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    star = models.PositiveSmallIntegerField() #12345로 제한
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1500)
    
    def __str__(self):
        return self.star + " : " + self.title


class WordStar(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    star1 = models.SmallIntegerField()
    star2 = models.SmallIntegerField()
    star3 = models.SmallIntegerField()
    star4 = models.SmallIntegerField()
    star5 = models.SmallIntegerField()
    all_star = models.IntegerField()
    avg_star = models.DecimalField(..., max_digits=5, decimal_places=4)
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word + " : " + self.avg_star

class WordSentiment(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    topic1 = models.DecimalField(..., max_digits=5, decimal_places=4)
    topic2 = models.DecimalField(..., max_digits=5, decimal_places=4)
    topic3 = models.DecimalField(..., max_digits=5, decimal_places=4)
    topic4 = models.DecimalField(..., max_digits=5, decimal_places=4)
    topic5 = models.DecimalField(..., max_digits=5, decimal_places=4)

    def __str__(self):
        return self.word