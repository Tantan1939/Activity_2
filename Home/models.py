from django.db import models
# Create your models here.


class Company_Images(models.Model):
    image = models.ImageField(default='default.jpg',
                              upload_to='Company_Images')


class Retail_Partners(models.Model):
    store_name = models.CharField(max_length=50)
    description = models.TextField()
    store_logo = models.ImageField(upload_to='Retail_Partners')

    def __str__(self):
        return self.store_name


class Products(models.Model):
    Product_name = models.CharField(max_length=50, primary_key=True)
    Product_description = models.TextField()
    Product_image = models.ImageField(upload_to='GPUs')
    Specifications = models.ForeignKey(
        'GPU_specs', on_delete=models.SET_NULL, null=True, blank=True)
    Date_added = models.DateTimeField(auto_now_add=True)
    Date_modified = models.DateTimeField(auto_now=True)
    Quantities = models.PositiveBigIntegerField()
    Price = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.Product_name


class GPU_specs(models.Model):
    GPU_model_name = models.ForeignKey(Products, on_delete=models.CASCADE)
    Graphic_engine = models.CharField(max_length=50)
    Bus_standard = models.CharField(max_length=50)
    OpenGL = models.CharField(max_length=50)
    Video_memory = models.CharField(max_length=50)
    Engine_clock = models.TextField()
    CUDA_core = models.CharField(max_length=50)
    Memory_speed = models.CharField(max_length=50)
    Memory_interface = models.CharField(max_length=50)
    Resolution = models.CharField(max_length=50)
    Interface = models.TextField()
    Maximum_display_support = models.PositiveIntegerField()
    Dimensions = models.TextField()
    Recommended_PSU = models.CharField(max_length=20)
    Power_connectors = models.CharField(max_length=20)
    Slot = models.CharField(max_length=20)

    def __str__(self):
        return self.Graphic_engine


class Questions(models.Model):
    Question = models.TextField()
    Answer = models.TextField()
