# Generated by Django 3.2.2 on 2021-05-11 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_curriculum_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencia',
            name='curriculum',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.curriculum'),
            preserve_default=False,
        ),
    ]
