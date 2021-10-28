from django.db   import models

from core.models import TimeStampedModel

class Menu(TimeStampedModel):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'menus'

class Category(TimeStampedModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    class Meta : 
        db_table = 'categories'

class Host(TimeStampedModel):
    name          = models.CharField(max_length=50)
    profile_image = models.URLField()
    
    class Meta : 
        db_table = 'hosts'
    
class Place(TimeStampedModel):
    category      = models.ForeignKey(Category, on_delete=models.CASCADE)
    host          = models.ForeignKey(Host, on_delete=models.CASCADE)
    city          = models.ForeignKey('City', on_delete=models.CASCADE)
    name          = models.CharField(max_length=50)
    price         = models.IntegerField()
    minimum_time  = models.IntegerField()
    description   = models.TextField()
    capacity      = models.CharField(max_length=50)
    size          = models.CharField(max_length=50)
    floor         = models.CharField(max_length=50)
    parking       = models.CharField(max_length=50)
    location_info = models.TextField()
    is_deleted    = models.BooleanField(default=False)
    
    class Meta : 
        db_table = 'places'
    
class Image(TimeStampedModel):  
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    url   = models.URLField()
    
    class Meta:
        db_table = 'images'
        
class City(TimeStampedModel):
    name = models.CharField(max_length=20)
    
    class Meta : 
        db_table = 'cities'    