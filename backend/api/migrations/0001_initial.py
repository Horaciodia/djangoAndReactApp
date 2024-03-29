# Generated by Django 4.1.7 on 2024-01-07 22:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=5)])),
                ('password', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=5)])),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
            ],
        ),
    ]
