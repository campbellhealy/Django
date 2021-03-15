"""BaseApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from countries.views import CountriesView, about, ProfileUpload  # , SearchResultsView
from leagues.views import LeaguesView, TeamResultsView
from teams.views import TeamsView, TeamStandingView, NextMatchView, TeamLineupView, TeamListView, TeamCreateView, TeamUpdateView
from players.views import PlayersView

# from countries.views import CountriesView, about

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", CountriesView, name="football_countries"),
    path("about/", about, name="football_about"),
    path("leagues/", LeaguesView, name="football_leagues"),
    path("results/", TeamResultsView, name="football_results"),
    path("teams/", TeamsView, name="football_teams"),
    path("standings/", TeamStandingView, name="team_standing"),
    path("nextmatch/", NextMatchView, name="next_match"),
    path("lineup/", TeamLineupView, name="the_lineup"),
    path("players/", PlayersView, name="football_players"),
    path("", include("countries.urls")),
    path('upload-csv/', ProfileUpload, name="profile_upload"),
    # path("search/", SearchResultsView, name="search_results"),
    path('change/', TeamListView.as_view(), name='team_changelist'),
    path('add/', TeamCreateView.as_view(), name='team_add'),
    path('<int:pk>/', TeamUpdateView.as_view(), name='team_change'),
]
