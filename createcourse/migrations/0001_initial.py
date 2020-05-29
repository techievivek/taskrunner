# Generated by Django 3.0.6 on 2020-05-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshopUsername', models.CharField(max_length=20)),
                ('yakshUsername', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopCached',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
