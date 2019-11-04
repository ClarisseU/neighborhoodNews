from django.db import models
from django.contrib.auth.models import User

# Create your models here.    
class NeighbourHood(models.Model):
    nName = models.CharField(max_length=60)
    nLocation = models.CharField(max_length=60)
    occupants = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.nName)
    
    def create_neighborhood(self):
        self.save()
    
    def delete_neighborhood(self):
        self.delete()
    
    @classmethod
    def find_neigborhood(cls,neigborhood_id):
        name = cls.objects.filter(nName = neigborhood_id)
        return name
    
    def update_neighborhood(self):
        self.update()
    
    def update_occupants():
        pass
    
class Business(models.Model):
    bName = models.CharField(max_length=60)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    hood_id = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True)
    buzz_email = models.CharField(max_length=60,null=True)
    
    def __str__(self):
        return str(self.bName)    
    
    def save_business(self):
        self.save()
        
    def delete_business(self):
        self.delete()
     
    @classmethod    
    def find_business(cls, business_id):
        pass
    
    def update_business(self):
        self.update()        
        
class Profile(models.Model): 
    picture = models.ImageField(upload_to='profile/', null=True)
    bio = models.CharField(max_length=60, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True) 
    
    def __str__(self):
        return str(self.bio)        
    
    def save_profile(self):
        self.save()