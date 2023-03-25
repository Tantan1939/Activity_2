import re
from django.shortcuts import render
from . models import Company_Images, Retail_Partners, Products, GPU_specs, Questions
from django.db.models.functions import Lower

# Create your views here.


def home(request):
    get_image = Company_Images.objects.get(pk=1)

    get_retail_stores = Retail_Partners.objects.select_related(
        None).order_by(Lower('store_name'))

    get_gpus = Products.objects.select_related(
        None).order_by('-Date_added')

    get_questions = Questions.objects.all().values().order_by(Lower('Question'))

    context = {
        'imagepath': get_image,
        'get_retail_stores': get_retail_stores,
        'get_gpus': get_gpus,
        'get_questions': get_questions,
    }

    return render(request, 'Home/Index.html', context)
