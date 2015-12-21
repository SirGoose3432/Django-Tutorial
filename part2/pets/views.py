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
    # There are two types of requests, GET and POST
    # Basically, GET requests are when data is being received from a page/vew
    # POST requests are when data is being sent to a page/view
    if request.method == 'GET':
        context = dict()
        # For a form, create a form and put it into the context
        context['form'] = PetForm()
        return render(request, 'pets/create_pet.html', context)
    elif request.method == 'POST':
        # Retrieve completed form data from the post request
        form = PetForm(request.POST)
        # Check if the form is valid or not
        if form.is_valid():
            # If the form is valid, save the data and redirect the user to the homepage
            form.save()
            return redirect('pets:home')
        else:
            # If the form is not valid, redirect the user to the same page for them to fill out the form again
            context = dict()
            # Use the same form that was created at the beginning of the POST request so that errors and data stay
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
