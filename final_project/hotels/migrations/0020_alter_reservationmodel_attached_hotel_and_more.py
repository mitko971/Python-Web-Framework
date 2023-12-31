# Generated by Django 4.2.3 on 2023-07-22 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0019_rename_attached_user_hotels_created_by_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='attached_hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotels.hotels'),
        ),
        migrations.AlterField(
            model_name='reservationmodel',
            name='attached_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reservation', to=settings.AUTH_USER_MODEL),
        ),
    ]
