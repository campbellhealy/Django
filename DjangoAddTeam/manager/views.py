from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Team, League
from .forms import TeamForm


class TeamListView(ListView):
    model = Team
    context_object_name = "teams"


class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("team_changelist")


class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy("team_changelist")


def load_leagues(request):
    country_id = request.GET.get("country")
    leagues = League.objects.filter(country_id=country_id).order_by("league_name")
    return render(
        request, "manager/league_dropdown_list_options.html", {"leagues": leagues}
    )
