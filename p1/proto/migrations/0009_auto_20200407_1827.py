# Generated by Django 3.0.5 on 2020-04-07 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0008_attraction_wc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attraction',
            old_name='wc',
            new_name='wordcloud',
        ),
    ]