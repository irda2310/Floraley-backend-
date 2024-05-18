from django.db import models
from django import forms
# Create your models here.

class Kategoria(models.Model):
    kategoria_id = models.AutoField(primary_key=True)
    kategoria_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.kategoria_type} - {self.kategoria_id}'
#coment

class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=50, null=True, blank=True)
    shop_color = models.CharField(max_length=50, null = True , blank=True)
    shop_review = models.TextField(max_length=1000, null=True, blank=True)
    shop_price = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True) 
    shop_img = models.ImageField(upload_to='food/')
    shop_category = models.ForeignKey(Kategoria, on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return f'{self.shop_name} - {self.shop_id}'

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title=models.TextField(max_length=1000, null=True, blank=True)
    blog_text=models.TextField(max_length=1000, null=True, blank=True)
    blog_img = models.ImageField(upload_to='blog/')
    blog_date=models.CharField(max_length=50, null = True , blank=True)
    def __str__(self):
        return f'{self.blog_title} - {self.blog_id}'

class Fullblog (models.Model):
    fullblog_id = models.AutoField(primary_key=True)
    fullblog_title=models.TextField(max_length=1000, null=True, blank=True)
    fullblog_text=models.TextField(max_length=1000, null=True, blank=True)
    fullblog_img = models.ImageField(upload_to='blog/')
    fullblog_date=models.CharField(max_length=50, null = True , blank=True)
    fullblog_img2 = models.ImageField(upload_to='blog/')
    fullblog_text2=models.TextField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return f'{self.fullblog_title} - {self.fullblog_id}'

class Contact (models.Model):
    contact_name=models.CharField(max_length=50, null=True, blank=True )    
    contact_message=models.TextField(max_length=500, null=True, blank=True)
    contact_email=models.EmailField(max_length=50, null=True, blank=True)
    def __str__(self):
        return f'{self.contact_name}'


class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} - {self.name}'
    
class Review (models.Model):
    review_name=models.CharField(max_length=50, null=True, blank=True )   
    review_job=models.TextField(max_length=500, null=True, blank=True) 
    review_message=models.TextField(max_length=500, null=True, blank=True)
    review_img = models.ImageField(upload_to='blog/')
    review_stars = models.TextField(max_length=1000, null=True, blank=True)

    
    def __str__(self):
        return f'{self.review_name}'