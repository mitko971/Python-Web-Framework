# Generated by Django 4.2.3 on 2023-08-06 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0021_alter_hotels_hotel_name_alter_hotels_location_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotels',
            options={'verbose_name': 'Хотели', 'verbose_name_plural': 'Хотели'},
        ),
        migrations.AlterModelOptions(
            name='reservationmodel',
            options={'verbose_name': 'Резервации', 'verbose_name_plural': 'Резервации'},
        ),
    ]
