from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Models):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.PhoneNumberField()
    
    
    
class Post(models.Model):
    image = models.CharField(max_length=500, blank=True, null=True)
    upload_image = models.ImageField(upload_to='post_image/', blank=True, null=True
    post_text = models.TextField(max_length=)
)