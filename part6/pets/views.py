from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import Pet, Owner
from .forms import PetForm, OwnerForm, LoginForm, UserForm


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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('pets:home')
                else:
                    context = dict()
                    return render(request, 'pets/login.html', context)
            else:
                context = dict()
                context['form'] = form
                return render(request, 'pets/login.html', context)
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
