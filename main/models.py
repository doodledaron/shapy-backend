from django.db import models

class Shape(models.Model):
    name = models.CharField(max_length=100)
    shape = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='shapes/', blank=True, null=True) #so that we could assign images later
    def __str__(self):
        return self.name
