from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models
from django.urls import reverse

from final_project.account.validators import validate_only_alphabetic


# Create your models here.
class AppUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The given username must be set")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomRegisterUser(AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    email = models.EmailField(
        blank=False,
        null=False,
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(2, ),
            validate_only_alphabetic,
        )
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        validators=(
            MinLengthValidator(2, ),
            validate_only_alphabetic,
        )
    )
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/',
    )

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('profile details', args=[str(self.pk)])



UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
