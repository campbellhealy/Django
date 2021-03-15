from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# from django.contrib.auth.models import User
# from django.views.generic import (
#     ListView,
#     # DetailView,
#     # CreateView,
# )
from .models import (
    Leagues,
)


def LeaguesView(request, *args, **kwargs):  # , ListView):
    return render(request, "leagues/leagues_home.html")  # , context)


def TeamResultsView(request):  # , DetailView):
    return render(request, "leagues/leagues_results.html", {"title": "Results"})
