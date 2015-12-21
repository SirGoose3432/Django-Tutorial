from django.shortcuts import render

from .models import Pet, Owner


# Example of a regular view
def pets_index(request):
    """
    Renders a page showing a list of owners and their pets
    :param request: request
    :return: render
    """
    # context is a python dictionary
    # context is used to take information from the database to the templates
    context = dict()
    # here we make a query to the database to get all the pets and all the owners and put them in the context
    context['owners'] = Owner.objects.all()
    context['pets'] = Pet.objects.all()
    # the render method allows us to render a page
    return render(request, 'pets/index.html', context)


def pets_home(request):
    """
    Renders the homepage of links to the rest of the pages
    :param request:
    :return: homepage
    """
    return render(request, 'pets/home.html')
