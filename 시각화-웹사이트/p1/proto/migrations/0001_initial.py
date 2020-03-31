# Generated by Django 2.1 on 2020-03-31 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('small_sort', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Big_Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.PositiveSmallIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=1500)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proto.Attraction')),
            ],
        ),
        migrations.CreateModel(
            name='WordSentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('topic1', models.DecimalField(decimal_places=4, max_digits=5)),
                ('topic2', models.DecimalField(decimal_places=4, max_digits=5)),
                ('topic3', models.DecimalField(decimal_places=4, max_digits=5)),
                ('topic4', models.DecimalField(decimal_places=4, max_digits=5)),
                ('topic5', models.DecimalField(decimal_places=4, max_digits=5)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proto.Attraction')),
            ],
        ),
        migrations.CreateModel(
            name='WordStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star1', models.SmallIntegerField()),
                ('star2', models.SmallIntegerField()),
                ('star3', models.SmallIntegerField()),
                ('star4', models.SmallIntegerField()),
                ('star5', models.SmallIntegerField()),
                ('all_star', models.IntegerField()),
                ('avg_star', models.DecimalField(decimal_places=4, max_digits=5)),
                ('word', models.CharField(max_length=50)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proto.Attraction')),
            ],
        ),
        migrations.AddField(
            model_name='attraction',
            name='big_sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proto.Big_Sort'),
        ),
    ]
