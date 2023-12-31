# Generated by Django 4.2.3 on 2023-08-11 16:51

from django.db import migrations, models
import final_project.hotels.validators


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0023_alter_hotels_reserve_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='days',
            field=models.PositiveIntegerField(validators=[final_project.hotels.validators.valid_days]),
        ),
    ]
