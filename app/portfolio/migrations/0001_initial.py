# Generated by Django 3.2.2 on 2021-05-11 17:36

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to=portfolio.models.cv_image_path)),
                ('educacion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tiempo_experiencia', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('certificados', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
