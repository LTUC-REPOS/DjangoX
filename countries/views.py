from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Country


class CountryListView(ListView):
    template_name ="countries/country_list.html"
    model = Country


class CountryDetailView(DetailView):
    template_name ="countries/country_detail.html"
    model = Country


class CountryCreateView(CreateView):
    template_name ="countries/country_create.html"
    model = Country
    fields = ["name","author","desc","captial"]


class CountryUpdateView(UpdateView):
    template_name ="countries/country_update.html"
    model = Country
    fields = ["name,","author","desc","captial"]


class CountryDeleteView(DeleteView):
    template_name ="countries/country_delete.html"
    model = Country
    success_url = reverse_lazy("country_list")