from django.db import models
from django.utils import timezone

from django.urls import reverse
from teams.models import Teams


class Players(models.Model):
    player_team = models.ForeignKey(
        Teams, verbose_name='Team', default=1, blank=True, on_delete=models.SET_DEFAULT)
    player_key = models.IntegerField(default=0000,  verbose_name='ID')
    player_name = models.CharField(
        max_length=30, default=None,  verbose_name='Name')
    player_number = models.IntegerField(
        default=0, blank=True,  verbose_name='shirt #')
    player_country = models.CharField(
        max_length=20, default=None, blank=True,  verbose_name='Country of Origin')
    player_type = models.CharField(
        max_length=15, default=None, blank=True,  verbose_name='Position')

    # date_now = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "players"

    def __str__(self):
        return self.player_name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
