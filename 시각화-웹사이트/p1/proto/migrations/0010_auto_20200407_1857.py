# Generated by Django 3.0.5 on 2020-04-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0009_auto_20200407_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='wordcloud',
            field=models.ImageField(blank=True, upload_to='proto/wc_image/'),
        ),
    ]
