# Generated by Django 4.2.3 on 2023-07-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0017_alter_reservationmodel_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservationmodel',
            old_name='attached_user',
            new_name='created_by_user',
        ),
    ]
