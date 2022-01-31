from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.fields.files import ImageField


class Category(models.Model):
    name = models.CharField(max_length=100, null=True )


    class Meta:
        verbose_name_plural = 'Category'


    def __str__(self):
        return self.name


class Property(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200 , null = True)
    price = models.IntegerField(null=True)
    img = models.ImageField(upload_to='PrimaryImages', null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.category.name + " : " + self.name


    class Meta:
        verbose_name_plural = 'Property'




class PropertyImages(models.Model):
    product = models.ForeignKey(Property, on_delete= models.CASCADE, null = True)
    product_img = models.ImageField(upload_to='images/product_images')

    class Meta:
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name



class Order(models.Model):
    product = models.ForeignKey(Property, on_delete= models.CASCADE, null = True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    


    def __str__(self):
        return self.product.name



