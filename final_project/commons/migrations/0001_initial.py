# Generated by Django 4.2.3 on 2023-07-06 08:13

import django.core.validators
from django.db import migrations, models
import final_project.account.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), final_project.account.validators.validate_only_alphabetic])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]