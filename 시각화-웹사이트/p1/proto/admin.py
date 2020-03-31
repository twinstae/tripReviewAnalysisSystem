from django.contrib import admin
from proto.models import Big_Sort, Attraction, WordStar, WordSentiment, Review

# Register your models here.
admin.site.register(Big_Sort)
admin.site.register(Review)
admin.site.register(Attraction)
admin.site.register(WordStar)
admin.site.register(WordSentiment)
