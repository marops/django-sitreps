# Generated by Django 2.0.6 on 2018-10-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitreps', '0010_auto_20181001_2121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitreps',
            options={'verbose_name_plural': 'SITREPS'},
        ),
        migrations.AlterField(
            model_name='sitreps',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='pub date'),
        ),
        migrations.AlterField(
            model_name='sitreps',
            name='title',
            field=models.CharField(default='SITREP 2018-10-02', max_length=200),
        ),
    ]
