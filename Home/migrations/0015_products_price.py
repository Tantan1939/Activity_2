# Generated by Django 4.0.1 on 2022-03-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_remove_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Price',
            field=models.FloatField(default=0),
        ),
    ]
