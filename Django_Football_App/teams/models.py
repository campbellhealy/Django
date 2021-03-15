from django.db import models
from django.utils import timezone

from django.urls import reverse
from countries.models import Countries
from leagues.models import Leagues


class Teams(models.Model):
    country_team = models.ForeignKey(
        Countries, verbose_name='Country', default=1, blank=True, on_delete=models.SET_NULL, null=True)
    league_team = models.ForeignKey(
        Leagues, verbose_name='League', default=1, blank=True, on_delete=models.SET_NULL, null=True)
    team_key = models.IntegerField(default=000000,  verbose_name='ID')
    team_name = models.CharField(max_length=30, blank=True)
    team_badge = models.URLField(blank=True,  verbose_name='Badge')

    class Meta:
        verbose_name_plural = "teams"

    def __str__(self):
        return self.team_name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class PlayersinTeam(Teams):
    '''import the players that could be in the team.'''
    #teams = models.ForeignKey(Teams, on_delete=models.CASCADE)
    pass


class Matches(Teams):
    '''List of the matches and dates for a team in the season'''
    # teams = models.ForeignKey(Teams, on_delete=models.CASCADE)
    pass


class LineUps(Teams):
    '''Lineup of players for a specific match'''
    # teams = models.ForeignKey(Teams, on_delete=models.CASCADE)
    pass


class Standings(Teams):
    ''' The results of the season to date'''
    # teams = models.ForeignKey(Teams, on_delete=models.CASCADE)
    pass
