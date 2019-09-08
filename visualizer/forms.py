from django import forms
from visualizer.models import Data

STATE_CHOICES = [
    ("AL", 'AL'),

    ("AK", 'AK'),

    ("AR", 'AR'),

    ("AZ", 'AZ'),

    ("CA", 'CA'),

    ("CO", 'CO'),

    ("CT", 'CT'),

    ("DC", 'DC'),

    ("DE", 'DE'),

    ("FL", 'FL'),

    ("GA", 'GA'),

    ("HI", 'HI'),

    ("IA", 'IA'),

    ("ID", 'ID'),

    ("IL", 'IL'),

    ("IN", 'IN'),

    ("KS", 'KS'),

    ("KY", 'KY'),

    ("LA", 'LA'),

    ("MA", 'MA'),

    ("MD", 'MD'),

    ("ME", 'ME'),

    ("MI", 'MI'),

    ("MN", 'MN'),

    ("MO", 'MO'),

    ("MS", 'MS'),

    ("MT", 'MT'),

    ("NC", 'NC'),

    ("NE", 'NE'),

    ("NH", 'NH'),

    ("NJ", 'NJ'),

    ("NM", 'NM'),

    ("NV", 'NV'),

    ("NY", 'NY'),

    ("ND", 'ND'),

    ("OH", 'OH'),

    ("OK", 'OK'),

    ("OR", 'OR'),

    ("PA", 'PA'),

    ("RI", 'RI'),

    ("SC", 'SC'),

    ("SD", 'SD'),

    ("TN", 'TN'),

    ("TX", 'TX'),

    ("UT", 'UT'),

    ("VT", 'VT'),

    ("VA", 'VA'),

    ("WA", 'WA'),

    ("WI", 'WI'),

    ("WV", 'WV'),

    ("WY", 'WY'),
]

YEAR_CHOICES = [
    ("2019", 2019),
    ("2018", 2018),
    ("2017", 2017),
    ("2016", 2016),
    ("2015", 2015),
    ("2014", 2014),
    ("2013", 2013),
    ("2012", 2012),
    ("2011", 2011),
    ("2010", 2010),
    ("2009", 2009),
    ("2008", 2008),
    ("2007", 2007),
    ("2006", 2006),
    ("2005", 2005),
    ("2004", 2004),
    ("2003", 2003),
    ("2002", 2002),
    ("2001", 2001),
    ("2000", 2000),
]

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ( 'year', 'state', 'population' )
        widgets = {
            'state': forms.Select(choices=STATE_CHOICES),
            'year': forms.Select(choices=YEAR_CHOICES),
        }

    def clean(self):
        cleaned_data = super().clean()

        year = cleaned_data.get('year')
        state = cleaned_data.get('state')
        population = cleaned_data.get('population')
        print("clean here")
        if not year:
            raise forms.ValidationError("year is required")
        if not state:
            raise forms.ValidationError("state is required")
        if not population:
            raise forms.ValidationError("population is required")
        if year < 2000 or year > 2019:
            raise forms.ValidationError("year out of range")

        return cleaned_data