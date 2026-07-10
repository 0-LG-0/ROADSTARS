from django.db import models

from django_ckeditor_5.fields import CKEditor5Field
from django.db.models import Q
from django.contrib.auth.models import User
# Create your models here.
    
class Post(models.Model):
    image_URL = models.CharField(max_length=500, blank=True, null=True)
    upload_image = models.ImageField(upload_to='post_image/', blank=True, null=True)
    post_text = CKEditor5Field(max_length=2000, blank=True, null=True, config_name='default')
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"User: {self.user.username} || Post: {self.id}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=(
                    Q(upload_image__isnull=False, image_URL__isnull=True) |
                    Q(image_URL__isnull=False, upload_image__isnull=True) |
                    Q(post_text__isnull=False)
                ), 
                name="Must submit something to create Post"
            )
        ]

class Event(models.Model):
    title = CKEditor5Field(max_length=200, config_name='default')
    image_URL = models.CharField(max_length=500, blank=True, null=True)
    upload_image = models.ImageField(upload_to='post_image/', blank=True, null=True)
    description = CKEditor5Field(max_length=2000, blank=True, null=True, config_name='default')
    instructions_and_rules = CKEditor5Field(max_length=1000, blank=True, null=True, config_name='default')
    address_and_contact = CKEditor5Field(default="Example: <p>Address: 0000 Street, City, State zipcode or ''Contact for Address'' <br />Email: example@gmail.com <br />Phone number: +1(111) 111-1111</p>", max_length=500, blank=True, null=True, config_name='default')
    participating_and_attending = CKEditor5Field( default="Example (for displaying): <p>Participating: 20/30 <br />Attending: 65/90</p>", max_length=500, blank=True, null=True, config_name='default')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateField()
    public = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    attendees = models.IntegerField(default=0, blank=True, null=True)
    participants = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return f"Event: {self.title} || Author: {self.user.username}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=(
                    Q(upload_image__isnull=False, image_URL__isnull=True) |
                    Q(image_URL__isnull=False, upload_image__isnull=True) |
                    Q(description__isnull=False) 
                ), 
                name="Must submit something to create Event",
            )
        ]