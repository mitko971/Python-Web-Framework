# Generated by Django 4.2.3 on 2023-07-10 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0012_reservationmodel_attached_hotel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='reserve_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservationmodel',
            name='attached_hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels'),
        ),
    ]
