# Generated by Django 2.0.6 on 2018-10-01 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitreps', '0007_auto_20181001_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitreps',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]