# Generated by Django 4.2.3 on 2023-07-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_alter_hotels_hotel_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='hotel_picture',
            field=models.ImageField(default='', upload_to='images/hotels/'),
            preserve_default=False,
        ),
    ]