from __future__ import unicode_literals

from django.db import models
  
class Product(models.Model):
    name = models.CharField(max_length=120)
 
    def __str__(self):
        return self.name
 
 
class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    programme = models.ForeignKey(Product)
    feedback = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.navn
