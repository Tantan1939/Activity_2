# Generated by Django 4.0.1 on 2022-03-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retail_Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('store_logo', models.ImageField(upload_to='Retail_Partners')),
            ],
        ),
    ]