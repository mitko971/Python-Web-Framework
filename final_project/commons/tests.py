from django.core.exceptions import ValidationError
from django.test import TestCase

from final_project.commons.models import Contact, Comments, ModelUser
from final_project.hotels.models import Hotels


# Create your tests here.

class ContactModelTest(TestCase):
    def test_valid_contact(self):
        contact = Contact.objects.create(
            first_name='Mitko',
            email='mitko1@abv.bg',
            description='Some'
        )
        self.assertEquals(contact.first_name, 'Mitko')
        self.assertEquals(contact.email, 'mitko1@abv.bg')
        self.assertEquals(contact.description, 'Some')

    def test_wrong_name(self):
        with self.assertRaises(ValidationError):
            contact = Contact.objects.create(
                first_name='mitko00',
                email='mitko@abv.bg',
                description='Some'
            )
            contact.full_clean()

    def test_blank_first_name(self):
        with self.assertRaises(ValidationError):
            contact = Contact.objects.create(
                first_name='',
                email='mitko@abv.bg',
                description='Some'
            )
            contact.full_clean()

    def test_blank_email(self):
        with self.assertRaises(ValidationError):
            contact = Contact.objects.create(
                first_name='Mitko',
                email='',
                description='Some'
            )
            contact.full_clean()

    def test_blank_description(self):
        with self.assertRaises(ValidationError):
            contact = Contact.objects.create(
                first_name='Mitko',
                email='mitko@abv.bg',
                description=''
            )
            contact.full_clean()

