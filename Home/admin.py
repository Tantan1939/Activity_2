from django.contrib import admin

from Home.models import Company_Images, GPU_specs, Products, Questions, Retail_Partners

# Register your models here.
admin.site.register(Company_Images)
admin.site.register(Retail_Partners)
admin.site.register(Products)
admin.site.register(GPU_specs)
admin.site.register(Questions)
