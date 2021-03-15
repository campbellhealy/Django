import csv
import io
import requests

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Countries


def ProfileUpload(request):
    # declaring template
    template = "countries/profile_upload.html"
    data = Countries.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be country_id, country_name, country_logo',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Countries.objects.update_or_create(
            country_id=column[0],
            country_name=column[1],
            country_logo=column[2],
        )
    context = {}
    return render(request, template, context)


def CountriesView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "countries/home.html")


def about(request):
    return render(request, "countries/about.html", {"title": "About"})

# def CountriesView(TemplateView):
#     template_name = "countries/home.html"
#     # return render(request, template_name)


class SearchResultsView(ListView):
    model = Countries
    template_name = "countries/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Countries.objects.filter(
            Q(country_id__icontains=query) | Q(country_name__icontains=query)
        )
        return object_list
