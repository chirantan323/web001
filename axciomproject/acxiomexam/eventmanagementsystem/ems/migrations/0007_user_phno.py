# Generated by Django 4.2.3 on 2023-10-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0006_vendor_phno'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phno',
            field=models.CharField(default='', max_length=12),
        ),
    ]
