from django.db import models

# Create your models here.


class Big_Sort(models.Model):
    sort_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sort_name


class Attraction(models.Model):
    name = models.CharField(max_length=100, unique=True)
    big_sort = models.ForeignKey(Big_Sort, on_delete=models.CASCADE)
    small_sort = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    star_info = models.CharField(max_length=100, null=True)
    review_sample = models.CharField(max_length=1500, null=True)
    cluster = models.PositiveSmallIntegerField(null = True)
    wordcloud = models.ImageField(blank=True, upload_to = "../static/image")
    
    def __str__(self):
        return self.name

class Route(models.Model):
    start_pk = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    end_pk = models.PositiveIntegerField()
    dist = models.PositiveIntegerField(null=True)
    direction = models.CharField(max_length=1500, null=True)
    
    def __str__(self):
        return str(self.start_pk) + " -> " + str(self.end_pk)

class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    star = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    date = models.DateField(blank=True, null=True)
    travelertype = models.CharField(max_length=10000, default = '')

    def __str__(self):
        return str(self.star) + " : " + str(self.title)


class WordStar(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    star1 = models.SmallIntegerField()
    star2 = models.SmallIntegerField()
    star3 = models.SmallIntegerField()
    star4 = models.SmallIntegerField()
    star5 = models.SmallIntegerField()
    all_star = models.IntegerField()
    avg_star = models.DecimalField(max_digits=5, decimal_places=4)
    word = models.CharField(max_length=50)

    def __str__(self):
        return str(self.word) + " : " + str(self.avg_star)


class WordSentiment(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    word = models.CharField(max_length=50, unique=True)
    topic1 = models.DecimalField(max_digits=5, decimal_places=4)
    topic2 = models.DecimalField(max_digits=5, decimal_places=4,null=True)
    topic3 = models.DecimalField(max_digits=5, decimal_places=4,null=True)
    topic4 = models.DecimalField(max_digits=5, decimal_places=4,null=True)
    topic5 = models.DecimalField(max_digits=5, decimal_places=4,null=True)

    def __str__(self):
        return str(self.word) + " : " + str(self.topic1)