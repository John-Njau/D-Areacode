from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    admin = models.ForeignKey(User, related_name='neighborhood_admin', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def create_neighborhood(self):
        self.save()
    
    def delete_neighborhood(self):
        self.delete()
        
    def find_neighborhood(self, neighborhood_id):
        return Neighborhood.objects.get(id=neighborhood_id)
    
    def update_neighborhood(self, name, location, occupants_count):
        self.name = name
        self.location = location
        self.occupants_count = occupants_count
        self.save()
    
    def get_occupants_count(self):
        return self.occupants_count
    
    def update_occupants(self, occupants_count):
        self.occupants_count = occupants_count
        self.save()
        
    def get_neighborhoods(self):
        return Neighborhood.objects.all()
    
    def __str__(self):
        return self.name
    
    
class Business(models.Model):
    user = models.ForeignKey(User, related_name='business_user', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, related_name='business_neighborhood', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField(max_length=1000)
    dated = models.DateTimeField(auto_now_add=True)
    
    def create_business(self):
        self.save()
        
    def delete_business(self, business_name, business_email):
        self.name = business_name
        self.email = business_email
        self.delete()
        
    def update_business(self, business_name, business_email):
        self.name = business_name
        self.email = business_email
        self.save()
    
    @classmethod
    def find_business(cls, business_id):
        businesses = cls.objects.filter(name__icontains=business_id)
        return businesses
    
    
    def __str__(self):
        return self.name
    