from django.urls import include, path

from .views import TeamListView, TeamCreateView, TeamUpdateView, load_leagues

urlpatterns = [
    path("", TeamListView.as_view(), name="team_changelist"),
    path("add/", TeamCreateView.as_view(), name="team_add"),
    path("<int:pk>/", TeamUpdateView.as_view(), name="team_change"),
    path("ajax/load-leagues/", load_leagues, name="ajax_load_leagues"),
]
