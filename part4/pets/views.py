from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, RequestContext

from .models import Pet, Owner
from .forms import PetForm, OwnerForm, LoginForm, UserForm


# the login decorator makes it where the user must be logged in before viewing the page
# if an unauthenticated user logs in then they will be redirected to the login page
# specified in settings.py
@login_required
def pets_index(request):
    """
    Renders a page showing a list of owners and their pets
    :param request:
    :return pets index page
    """
    context = dict()
    context['owners'] = Owner.objects.all()
    context['pets'] = Pet.objects.all()
    return render(request, 'pets/index.html', context)


@login_required
def pets_home(request):
    """
    Renders the homepage of links to the rest of the pages
    :param request:
    :return: homepage
    """
    return render(request, 'pets/home.html')


@login_required
def create_pet(request):
    """
    Renders a page that displays a form to create and save a new pet object
    :param request:
    :return:
    """
    if request.method == 'GET':
        context = dict()
        context['form'] = PetForm()
        return render(request, 'pets/create_pet.html', context)
    elif request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pets:home')
        else:
            context = dict()
            context['form'] = form
            return render(request, 'pets/create_pet.html', context)


@login_required
def create_owner(request):
    """
    Renders a page that displays a form to create and save a new owner object
    :param request:
    :return:
    """
    if request.method == 'GET':
        context = dict()
        context['form'] = OwnerForm()
        return render(request, 'pets/create_owner.html', context)
    elif request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pets:home')
        else:
            context = dict()
            context['form'] = form
            return render(request, 'pets/create_owner.html', context)


# Creating a user is just like creating any other object with a form
def create_user(request):
    """
    Renders a page that displays a form to create a user using the built
    :param request:
    :return:
    """
    if request.method == 'GET':
        context = dict()
        context['form'] = UserForm()
        return render(request, 'pets/create_user.html', context)
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pets:login')
        else:
            context = dict()
            context['form'] = form
            return render(request, 'pets/create_user.html', context)


@login_required
def user_info(request):
    """
    Renders a page that shows the information of the currently logged in user
    :param request:
    :return:
    """
    # We don't have to pass in a context dictionary here
    # Information regarding the current user is already stored in the session
    return render(request, 'pets/user_info.html')


def user_login(request):
    """
    Login page to login and authenticate users
    :param request:
    :return:
    """
    if request.method == 'GET':
        context = dict()
        context['form'] = LoginForm()
        return render(request, 'pets/login.html', context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # To get data from a form is must be validated by is_valid()
            # Then data can be accessed like below
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # The authenticate method checks if the given username and password combo are valid
            # If it is valid, it returns a reference to a user object
            user = authenticate(username=username, password=password)
            if user is not None:
                # User has the attribute is_active which is a boolean
                # If it is false, the user cannot log into the site
                if user.is_active:
                    # the login method logs in a valid user
                    login(request, user)
                    return redirect('pets:home')
                else:
                    # If the user is not active, redirect them back to the login page
                    context = dict()
                    return render(request, 'pets/login.html', context)
            # If the login credentials do not match, redirect the user back to the login page
            else:
                context = dict()
                context['form'] = form
                return render(request, 'pets/login.html', context)
        # if the form hasn't been filled out correctly, redirect the user back to the login page
        else:
            context = dict()
            context['form'] = form
            return render(request, 'pets/login.html', context)


def user_logout(request):
    """
    Logout method that returns the user to the login page
    :param request:
    :return:
    """
    logout(request)
    return redirect('pets:login')
