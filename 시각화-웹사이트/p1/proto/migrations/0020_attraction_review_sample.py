# Generated by Django 3.0.6 on 2020-06-09 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0019_auto_20200609_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='review_sample',
            field=models.CharField(max_length=1500, null=True),
        ),
    ]
