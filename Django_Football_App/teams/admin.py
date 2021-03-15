from django.contrib import admin

from .models import Teams


class TeamsAdmin(admin.ModelAdmin):
    list_display = ('country_team', 'league_team',
                    'team_key', 'team_name', 'team_badge')


admin.site.register(Teams, TeamsAdmin)
