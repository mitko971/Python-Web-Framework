# Generated by Django 4.2.3 on 2023-08-11 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0022_alter_hotels_options_alter_reservationmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='reserve_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
