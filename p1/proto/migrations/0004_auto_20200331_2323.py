# Generated by Django 2.1 on 2020-03-31 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0003_auto_20200331_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='attraction',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]