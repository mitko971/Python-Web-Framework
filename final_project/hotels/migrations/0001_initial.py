# Generated by Django 4.2.3 on 2023-07-06 12:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=30, unique=True)),
                ('location', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('choices', models.CharField(choices=[('All inclusive', 'All inclusive'), ('Not all inclusive', 'Not all inclusive')], max_length=20)),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('picture', models.URLField()),
                ('attached_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Hotel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]