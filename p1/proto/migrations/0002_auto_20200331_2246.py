# Generated by Django 2.1 on 2020-03-31 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='attraction',
            name='small_sort',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='wordsentiment',
            name='topic2',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='wordsentiment',
            name='topic3',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='wordsentiment',
            name='topic4',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='wordsentiment',
            name='topic5',
            field=models.DecimalField(decimal_places=4, max_digits=5, null=True),
        ),
    ]