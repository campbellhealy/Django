from django.db import models
from django.utils import timezone

from django.urls import reverse
from countries.models import Countries


class Leagues(models.Model):
    country_league = models.ForeignKey(
        Countries, verbose_name='Country', default=1, blank=True, on_delete=models.SET_DEFAULT)
    league_id = models.IntegerField(default=20,  verbose_name='ID')
    league_name = models.CharField(max_length=20)
    league_season = models.CharField(
        max_length=20, blank=True,  verbose_name='Season')
    league_logo = models.URLField(blank=True,  verbose_name='Logo')
    # country_logo = models.CharField(max_length=90, blank=True)

    class Meta:
        verbose_name_plural = "leagues"

    def __str__(self):
        return self.league_name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class TeamInLeague(models.Model):
    # Import the Teams that could be in a league???
    pass
