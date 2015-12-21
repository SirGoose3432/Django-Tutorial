from django import forms

from .models import Pet, Owner


# ModelForm are is a type of form that directly corresponds to a model
class PetForm(forms.ModelForm):
    """
    Form for creating a pet object
    """

    class Meta:
        # Set the model that the form corresponds to
        model = Pet
        # Set the desired fields that the form should have
        fields = ['name', 'type', 'owner', 'age']


class OwnerForm(forms.ModelForm):
    """
    Form for creating an owner object
    """

    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'dob', 'favorite_pet_type']
