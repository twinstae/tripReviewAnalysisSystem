# Generated by Django 3.0.5 on 2020-06-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0015_auto_20200429_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='travelertype_business',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='review',
            name='travelertype_couple',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='review',
            name='travelertype_family',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='review',
            name='travelertype_friend',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='review',
            name='travelertype_solo',
            field=models.CharField(default='', max_length=10000),
        ),
    ]