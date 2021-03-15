from django.forms import ModelForm
from .models import Countries


class CountriesForm(ModelForm):
    class Meta:
        model = Countries
        fields = [
            "country_id",
            "country_name",
            'country_logo',
        ]
