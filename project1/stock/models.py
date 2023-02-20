from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300)
    image = models.ImageField(upload_to='product_images')
    description = models.TextField()

    def __str__(self) : 
        return self.name

class Product(models.Model) :
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    avalable = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name
    
    