# Generated by Django 4.2.3 on 2023-10-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0004_user_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='category',
        ),
        migrations.AddField(
            model_name='vendor',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
    ]