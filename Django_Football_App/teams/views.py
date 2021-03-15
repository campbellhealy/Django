from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
# from .forms import TeamsForm
from .models import (
    Teams,
)

# from django.views.generic import (
#     ListView,
#     # DetailView,
#     # CreateView,
# )


def TeamsView(request):  # , DetailsView):
    # form = TeamsForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = TeamsForm()
    # context = {"form": form}
    return render(request, "teams/teams_home.html")  # , context)


# Testing for Chainlink Dropdowns
class TeamListView(ListView):
    model = Teams
    context_object_name = 'team'


class TeamCreateView(CreateView):
    model = Teams
    fields = ('country_team', 'league_team', 'team_key',
              'team_key', 'team_name', 'team_badge')
    success_url = reverse_lazy('team_changelist')


class TeamUpdateView(UpdateView):
    model = Teams
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('Team_changelist')
# End of Testing for Chainlink Dropdowns


def TeamStandingView(request):  # , ListView):
    return render(request, "teams/teams_standings.html", {"title": "The Standings"})


def NextMatchView(request):  # , DetailView):
    return render(request, "teams/teams_next_matches.html", {"title": "Next Matches"})


def TeamLineupView(request):  # , DetailView):
    return render(request, "teams/teams_lineup.html", {"title": "Line Up"})
