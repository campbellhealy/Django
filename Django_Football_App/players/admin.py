from django.contrib import admin

from .models import Players


class PlayersAdmin(admin.ModelAdmin):
    list_display = ('player_team', 'player_key', 'player_name',
                    'player_number', 'player_country', 'player_type')


admin.site.register(Players, PlayersAdmin)
