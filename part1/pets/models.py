from __future__ import unicode_literals

from django.db import models


class Owner(models.Model):
    """
    A class representing the owner of a pet
    add a to string
    """
    PET_TYPE_CHOICES = {
        ("None", "None"),
        ("Cat", "Cat"),
        ("Dog", "Dog"),
        ("Rabbit", "Rabbit"),
        ("Hamster", "Hamster"),
        ("Gerbil", "Gerbil"),
        ("Bird", "Bird"),
    }

    # If a field is not optional, it must have a default value otherwise errors will occur when making migrations
    first_name = models.CharField('First Name', max_length=50, default=' ')
    last_name = models.CharField('Last Name', max_length=50, default=' ')
    dob = models.DateField('Date of Birth')
    # The field favorite_pet_type is optional since the parameter blank is set to True
    # Fields can be given choices to choose from
    favorite_pet_type = models.CharField('Favorite Type of Pet', max_length=50, choices=PET_TYPE_CHOICES, blank=True)

    def __str__(self):
        """
        this is a method for the class that returns a string representation of the object
        without this, in some cases an Owner object would simply show as 'Owner object'
        :return: the combination of the first and last names of an owner
        """
        return self.first_name + " " + self.last_name


class Pet(models.Model):
    """
    A class representing an animal that is a pet
    """
    PET_TYPE_CHOICES = {
        ("Cat", "Cat"),
        ("Dog", "Dog"),
        ("Rabbit", "Rabbit"),
        ("Hamster", "Hamster"),
        ("Gerbil", "Gerbil"),
        ("Bird", "Bird"),
    }

    name = models.CharField('Name', max_length=50, default=' ')
    type = models.CharField('Type', max_length=30, choices=PET_TYPE_CHOICES)
    # ForeignKeys represent many-to-one relations.
    # Here a Pet can have one Owner, but an Owner can have many pets.
    owner = models.ForeignKey('Owner', Owner)
    # PositiveIntegerField ensures that entries are > 0
    age = models.PositiveIntegerField('Age', default=0)
