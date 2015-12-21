from django.shortcuts import render, redirect

from .models import Pet, Owner
from .forms import PetForm, OwnerForm


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


def pets_home(request):
    """
    Renders the homepage of links to the rest of the pages
    :param request:
    :return: homepage
    """
    return render(request, 'pets/home.html')


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
