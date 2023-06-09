# Generated by Django 4.0.1 on 2022-03-01 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_retail_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('Product_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Product_description', models.TextField()),
                ('Product_image', models.ImageField(upload_to='GPUs')),
                ('Specifications', models.TextField()),
                ('Date_added', models.DateTimeField(auto_now_add=True)),
                ('Date_modified', models.DateTimeField(auto_now=True)),
                ('Quantities', models.PositiveBigIntegerField()),
            ],
        ),
    ]
