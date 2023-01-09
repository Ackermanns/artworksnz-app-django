from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    primary_media = models.CharField(max_length=40)
    
#NOTE:
#on foreign key "on_delete=models.CASCADE" means when artist is removed,
#all Artworks from the associated artist are removed as well
#This is also useful because it clears out images not being used, bloating storage over time.

class Artwork(models.Model):
    artwork = models.CharField(max_length=40)
    media_type = models.CharField(max_length=40)
    completion_date = models.DateField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    note = models.TextField()
    artwork_img = models.ImageField(null=True, blank=True, upload_to ='uploads/')
    artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE)