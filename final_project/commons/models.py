from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from final_project.account.validators import validate_only_alphabetic
from final_project.hotels.models import Hotels

# Create your models here.

ModelUser = get_user_model()


class Contact(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(2, ),
            validate_only_alphabetic,
        )
    )
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True,
    )
    description = models.TextField(
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = 'Контакти'
        verbose_name_plural = 'Контакти'


class Comments(models.Model):
    description = models.TextField(
        max_length=250,
        blank=False,
        null=False,
    )
    user = models.ForeignKey(
        ModelUser,
        on_delete=models.DO_NOTHING,
    )
    hotel = models.ForeignKey(
        Hotels,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Коментари'
        verbose_name_plural = 'Коментари'
