# Generated by Django 2.2.6 on 2019-11-01 11:51

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_example2model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example2model',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
