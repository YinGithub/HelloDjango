from django.views.generic import ListView,DetailView
from models import *


def city_detail(request, slug, **kwargs):
    return DetailView(
        request,
        queryset=City.objects.all(),
        slug=slug,
        **kwargs
    )
city_detail.__doc__ = DetailView.__doc__


def city_list(request, **kwargs):
    return ListView(
        request,
        queryset=City.objects.all(),
        paginate_by=20,
        **kwargs
    )
city_list.__doc__ = ListView.__doc__


def place_type_detail(request, slug, **kwargs):
    return DetailView(
        request,
        queryset=PlaceType.objects.all(),
        slug=slug,
        **kwargs
    )
place_type_detail.__doc__ = DetailView.__doc__


def place_type_list(request, **kwargs):
    return ListView(
        request,
        queryset=PlaceType.objects.all(),
        paginate_by=20,
        **kwargs
    )
place_type_list.__doc__ = ListView.__doc__


def place_detail(request, slug, **kwargs):
    return DetailView(
        request,
        queryset=Place.objects.all(),
        slug=slug,
        **kwargs
    )
place_detail.__doc__ = DetailView.__doc__


def place_list(request, **kwargs):
    return ListView(
        request,
        queryset=Place.objects.all(),
        paginate_by=20,
        **kwargs
    )
place_list.__doc__ = ListView.__doc__
