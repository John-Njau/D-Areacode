from django.db import models

from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField

import datetime as dt

from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post = models.TextField()
    image = CloudinaryField('photo', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.post
    
    class Meta:
        ordering = ('-created_on',)
        
    @classmethod
    def search_post(cls, search_term):
        results = cls.objects.filter(name__icontains=search_term)
        return results
    
class Neighborhood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    occupants_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def create_neighborhood(self):
        self.save()
    
    def delete_neighborhood(self):
        self.delete()
    
    @classmethod
    def find_neighborhood(cls, search_term):
        results = cls.objects.filter(name__icontains=search_term)
        return results
    
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
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,default=1, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = CloudinaryField('image', default='https://res.cloudinary.com/dkxq0qjqb/image/upload/v1624098981/default_avatar_qjqjq.png')
    
    def __str__(self):
        return f'{self.user.username} profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
            
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
        
    
    # def get_absolute_url(self):
    #     return reverse('profile', args=[str(self.id)])
    

class Business(models.Model):
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
    def find_business(cls, search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses
    
    
    def __str__(self):
        return self.name
    
    
class SocialAmenities(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, related_name='amenity', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=255)
    
    def create_amenity(self):
        self.save()
        
    def delete_amenity(self, amenity_name, amenity_email):
        self.name = amenity_name
        self.email = amenity_email
        self.delete()
        
    def update_amenity(self, amenity_name, amenity_email):
        self.name = amenity_name
        self.email = amenity_email
        self.save()
    
    @classmethod
    def find_amenity(cls, search_term):
        amenityes = cls.objects.filter(name__icontains=search_term)
        return amenityes
    
    
    def __str__(self):
        return self.name
    
    
