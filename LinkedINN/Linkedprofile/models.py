from django.db import models

# Create your models here.class Banner(models.Model):
class logo(models.Model):
    title = models.CharField(max_length=100)
    banner_image=models.ImageField(upload_to='product/banner')
    def  __str__(self):
        return self.title
    
class mains(models.Model):
    title = models.CharField(max_length=100)
    photo=models.ImageField(upload_to='product/banner')
    def  __str__(self):
        return self.title