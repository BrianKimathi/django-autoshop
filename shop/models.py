from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True)  # Assuming single main image
    # Use ManyToManyField for multiple images
    images = models.ManyToManyField('ProductImage', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    discount = models.PositiveIntegerField(default=0)  # Discount as a percentage
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE)  # Renamed field
    image = models.FileField(upload_to='products/')  # For storing individual product images

    def __str__(self):
        return f"{self.product_item.title} - Image"

class Comment(models.Model):
    name = models.CharField(max_length=255)
    comment_text = models.TextField()
    
    def __str__(self):
        return f"{self.name}"
    

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=300)
    message = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.name}"



class Slide(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='slides/')

    def __str__(self):
        return self.title
    
class Vehicle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='vehicles/')

    def __str__(self):
        return self.title