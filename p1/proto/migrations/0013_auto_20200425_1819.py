# Generated by Django 3.0.5 on 2020-04-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0012_auto_20200407_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='wordcloud',
            field=models.ImageField(blank=True, upload_to='../static/proto/static'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=3000),
        ),
    ]