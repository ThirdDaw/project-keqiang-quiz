# Generated by Django 3.0.5 on 2020-04-03 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='answers/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/', verbose_name='Image'),
        ),
    ]
