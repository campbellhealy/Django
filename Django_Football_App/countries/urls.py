# countries/urls.py

from .views import CountriesView, SearchResultsView, ProfileUpload
from django.urls import path, include


urlpatterns = [
    path("search/", SearchResultsView.as_view(), name="search_results"),
    # path("", CountriesView.as_view(), name="countries_home"),
    # path("", include("countries.urls"),  name="football_countries"),
]
