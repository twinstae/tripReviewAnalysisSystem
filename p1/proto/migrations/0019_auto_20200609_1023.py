# Generated by Django 3.0.6 on 2020-06-09 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0018_auto_20200606_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='star_info',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='wordcloud',
            field=models.ImageField(blank=True, upload_to='../static/image'),
        ),
    ]