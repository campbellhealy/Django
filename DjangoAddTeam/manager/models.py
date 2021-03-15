from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class League(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    league_name = models.CharField(max_length=30)

    def __str__(self):
        return self.league_name


class Team(models.Model):
    team_name = models.CharField(max_length=100, verbose_name="Team")
    birthdate = models.DateField(null=True, blank=True, verbose_name="Established")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    league_name = models.ForeignKey(
        League, on_delete=models.SET_NULL, null=True, verbose_name="League"
    )

    def __str__(self):
        return self.team_name
