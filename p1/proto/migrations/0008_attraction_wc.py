# Generated by Django 3.0.5 on 2020-04-03 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0007_auto_20200403_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='wc',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]