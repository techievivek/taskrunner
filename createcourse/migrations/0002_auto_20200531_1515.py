# Generated by Django 3.0.6 on 2020-05-31 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('createcourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermap',
            old_name='workshopUsername',
            new_name='workshop_user',
        ),
        migrations.RenameField(
            model_name='usermap',
            old_name='yakshUsername',
            new_name='yaksh_user',
        ),
        migrations.AddField(
            model_name='workshopcached',
            name='cached_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshopcached',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Success'), (2, 'Failed')], default=0),
        ),
    ]