# Generated by Django 2.2.6 on 2019-11-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191101_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example2model',
            name='phone_number',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
