from django import forms
from visualizer.models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ( 'year', 'state', 'population' )

    def clean(self):
        cleaned_data = super().clean()

        year = cleaned_data.get('year')
        state = cleaned_data.get('state')
        population = cleaned_data.get('population')
        if not year:
            raise forms.ValidationError("Invalid content")

        return cleaned_data