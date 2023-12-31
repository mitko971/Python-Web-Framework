# Generated by Django 4.2.3 on 2023-07-20 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0019_rename_attached_user_hotels_created_by_user_and_more'),
        ('commons', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='hotel',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
