from django import forms
from .models import Team, League


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("team_name", "birthdate", "country", "league_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["league_name"].queryset = League.objects.none()

        if "country" in self.data:
            try:
                country_id = int(self.data.get("country"))
                self.fields["league_name"].queryset = League.objects.filter(
                    country_id=country_id
                ).order_by("country")
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields["league"].queryset = self.instance.country.league_set.order_by(
                "name"
            )
