# Generated by Django 4.0.1 on 2022-03-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Price',
            field=models.FloatField(),
        ),
    ]
