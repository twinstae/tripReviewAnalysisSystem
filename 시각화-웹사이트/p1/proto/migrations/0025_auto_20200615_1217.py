# Generated by Django 3.0.6 on 2020-06-15 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0024_auto_20200612_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='star_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
