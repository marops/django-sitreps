# Generated by Django 2.0.6 on 2018-10-01 20:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sitreps', '0006_auto_20181001_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitreps',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitreps',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
