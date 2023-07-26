# Generated by Django 4.2.3 on 2023-07-20 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0019_rename_attached_user_hotels_created_by_user_and_more'),
        ('commons', '0003_comments_hotel_alter_comments_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotels.hotels'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
