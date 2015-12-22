from django.test import TestCase

from .models import Owner, Pet


# Important documentation for testing
# https://docs.djangoproject.com/en/1.9/topics/testing/overview/

class OwnerTestCase(TestCase):
    """
    Test the creation of several owners
    """

    # In setUp, all models that are going to be used are created
    # Objects created here are not saved to the database
    def setUp(self):
        Owner.objects.create(first_name='Steve', last_name='Jobs', dob='1955-02-24', favorite_pet_type='Dog')
        Owner.objects.create(first_name='Bill', last_name='Gates', dob='1955-10-28', favorite_pet_type='Cat')
        Owner.objects.create(first_name='Linus', last_name='Torvalds', dob='1969-12-28', favorite_pet_type='Bird')

    def test_owner_to_string(self):
        """
        Test to see if the __str__ method for Owner objects works
        """
        steve = Owner.objects.get(first_name='Steve')
        bill = Owner.objects.get(first_name='Bill')
        linus = Owner.objects.get(first_name='Linus')
        # use assert methods found in python3.4/unittest/case.py to create unit tests
        self.assertEquals(steve.__str__(), "Steve Jobs")
        self.assertEquals(bill.__str__(), "Bill Gates")
        self.assertEquals(linus.__str__(), "Linus Torvalds")


class OwnerPetTestCase(TestCase):
    """
    Test the creation of several owner objects and pets
    """

    def setUp(self):
        o1 = Owner.objects.create(first_name='Steve', last_name='Jobs', dob='1955-02-24', favorite_pet_type='Dog')
        o2 = Owner.objects.create(first_name='Bill', last_name='Gates', dob='1955-10-28', favorite_pet_type='Cat')
        o3 = Owner.objects.create(first_name='Linus', last_name='Torvalds', dob='1969-12-28', favorite_pet_type='Bird')
        Pet.objects.create(name='Odie', type='Dog', owner=o1, age=12)
        Pet.objects.create(name='Garfield', type='Cat', owner=o2, age=12)
        Pet.objects.create(name='Tux', type='Bird', owner=o3, age=19)

    def test_owners_have_pets(self):
        """
        Test that owners can pets that are related to them
        :return:
        """
        odie = Pet.objects.get(name='Odie')
        garfield = Pet.objects.get(name='Garfield')
        tux = Pet.objects.get(name='Tux')
        steve = Owner.objects.get(first_name='Steve')
        bill = Owner.objects.get(first_name='Bill')
        linus = Owner.objects.get(first_name='Linus')
        self.assertEquals(odie.owner, steve, "Odie is owned by Steve")
        self.assertEquals(garfield.owner, bill, "Garfield is owned by Bill")
        self.assertEquals(tux.owner, linus, "Tux is owned by Linus")
