# Generated by Django 4.0.1 on 2022-03-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0016_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Price',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
