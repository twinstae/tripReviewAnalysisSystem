# Generated by Django 3.0.5 on 2020-04-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0013_auto_20200425_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=10000),
        ),
    ]
