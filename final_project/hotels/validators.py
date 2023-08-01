from django.core.exceptions import ValidationError


def hotel_name_validators(value):
    for v in value:
        if not v.isalpha():
            raise ValidationError('Името трябва да съдържа само букви')


def location_name_validators(value):
    for v in value:
        if not v.isalpha():
            raise ValidationError('Локацията трябва да съдържа само букви')
