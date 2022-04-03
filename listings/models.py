from django.db import models

class Listing(models.Model):
    # item descriptions
    title = models.CharField(max_length=250)
    number = models.IntegerField(null=True)
    description = models.TextField()
    
    # price descriptions
    price = models.FloatField()
    price_fixed = models.BooleanField(default=False)

    # posted information
    posted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
