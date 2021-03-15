from django.contrib import admin

from .models import Leagues


class LeaguesAdmin(admin.ModelAdmin):
    list_display = ('country_league', 'league_id',
                    'league_name', 'league_season', 'league_logo')


admin.site.register(Leagues, LeaguesAdmin)
