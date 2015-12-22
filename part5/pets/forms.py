from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

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


class UserForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, with a first_name, last_name,
    username, email, and password.
    Most of this form is copied from the built in UserCreation form found in
    django.contrib.auth.forms.UserCreationForm
    What is added is first_name, last_name, and email.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    # Extra fields can be added to model forms as well
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as before, for verification."))

    class Meta:
        model = User
        # In the meta, fields that are from the model are written here
        fields = ("username", "email", "first_name", "last_name")

    # cleaning data is done below
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
            )
        self.instance.username = self.cleaned_data.get('username')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    # each form has a save method. it can be override and changed like below.
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# This is a regular form. It doesn't correspond to a model so doesn't have a meta section like a ModelForm
class LoginForm(forms.Form):
    """
    Form for getting fields necessary for a login
    """
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
