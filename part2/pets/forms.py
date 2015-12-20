from django import forms

from .models import Pet, Owner


class PetForm(forms.ModelForm):
    """
    Form for creating a pet object
    """

    class Meta:
        model = Pet
        fields = ['name', 'type', 'owner', 'age']


class OwnerForm(forms.ModelForm):
    """
    Form for creating an owner object
    """

    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'dob', 'favorite_pet_type']
