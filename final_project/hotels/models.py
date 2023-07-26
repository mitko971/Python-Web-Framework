from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from final_project.account.models import Profile

# Create your models here.
User = get_user_model()


class Hotels(models.Model):
    hotel_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
    )
    location = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )
    price = models.IntegerField(
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
    )


class ReservationModel(models.Model):
    CHOICES = (
        ('All inclusive', 'All inclusive'),
        ('Not all inclusive', 'Not all inclusive'),
    )

    days = models.PositiveIntegerField(
        null=False,
        blank=False,
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

    def __str__(self):
        return f"{self.choices} {self.attached_user}"

    def get_absolute_url(self):
        return reverse('user reservation', args=[str(self.pk)])
