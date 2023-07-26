from django.core.exceptions import ValidationError


def validate_only_alphabetic(value):
    for v in value:
        if not v.isalpha():
            raise ValidationError('Невалидно име: (само букви)!')