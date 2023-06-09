# Generated by Django 4.0.1 on 2022-03-01 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPU_specs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Graphic_engine', models.CharField(max_length=50)),
                ('Bus_standard', models.CharField(max_length=50)),
                ('OpenGL', models.CharField(max_length=50)),
                ('Video_memory', models.CharField(max_length=50)),
                ('Engine_clock', models.TextField()),
                ('CUDA_core', models.CharField(max_length=50)),
                ('Memory_speed', models.CharField(max_length=50)),
                ('Memory_interface', models.CharField(max_length=50)),
                ('Resolution', models.CharField(max_length=50)),
                ('Interface', models.TextField()),
                ('Maximum_display_support', models.PositiveIntegerField()),
                ('Dimensions', models.TextField()),
                ('Recommended_PSU', models.CharField(max_length=20)),
                ('Power_connectors', models.CharField(max_length=20)),
                ('Slot', models.CharField(max_length=20)),
                ('GPU_model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.products')),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='Specifications',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Home.gpu_specs'),
        ),
    ]
