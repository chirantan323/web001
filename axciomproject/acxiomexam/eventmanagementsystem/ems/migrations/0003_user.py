# Generated by Django 4.2.3 on 2023-10-10 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0002_admin1'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]