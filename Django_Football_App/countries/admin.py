from django.contrib import admin


from .models import Countries


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country_name', 'country_logo')


admin.site.register(Countries, CountryAdmin)
