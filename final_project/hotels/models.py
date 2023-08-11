from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from final_project.account.models import Profile
from final_project.hotels.validators import hotel_name_validators, location_name_validators, valid_days

# Create your models here.
User = get_user_model()


class Hotels(models.Model):
    hotel_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
        validators=(
            hotel_name_validators,
        )
    )
    location = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=(
            location_name_validators,
        )
    )

    description = models.TextField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )

    stars = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(1, ),
            MaxValueValidator(5, ),
        )
    )
    hotel_picture = models.ImageField(
        null=False,
        blank=False,
        upload_to='images/hotels/',
    )
    created_by_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="Hotel",
        null=True,
    )
    reserve_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Хотели'
        verbose_name_plural = 'Хотели'

    def __str__(self):
        return self.hotel_name


class ReservationModel(models.Model):
    CHOICES = (
        ('All inclusive', 'All inclusive'),
        ('Not all inclusive', 'Not all inclusive'),
    )

    days = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            valid_days,
        )
    )

    choices = models.CharField(
        max_length=20,
        choices=CHOICES,
        null=False,
        blank=False,
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    attached_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="reservation",
        null=True,
        blank=True,
    )
    attached_hotel = models.ForeignKey(
        Hotels,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Резервации'
        verbose_name_plural = 'Резервации'

    def __str__(self):
        return f"{self.choices} {self.attached_user}"

    def get_absolute_url(self):
        return reverse('user reservation', args=[str(self.pk)])
