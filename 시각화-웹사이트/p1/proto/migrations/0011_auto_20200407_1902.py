# Generated by Django 3.0.5 on 2020-04-07 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0010_auto_20200407_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='small_sort',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
