from django.db import models

STATE_CHOICES = [
("AL" , 'AL'),
 
("AK" , 'AK'),
 
("AR" , 'AR'),
 
("AZ" , 'AZ'),
 
("CA" , 'CA'),
 
("CO" , 'CO'),
 
("CT" , 'CT'),
 
("DC" , 'DC'),
 
("DE" , 'DE'),
 
("FL" , 'FL'),
 
("GA" , 'GA'),
 
("HI" , 'HI'),
 
("IA" , 'IA'),
 
("ID" , 'ID'),
 
("IL" , 'IL'),
 
("IN" , 'IN'),
 
("KS" , 'KS'),
 
("KY" , 'KY'),
 
("LA" , 'LA'),
 
("MA" , 'MA'),
 
("MD" , 'MD'),
 
("ME" , 'ME'),
 
("MI" , 'MI'),
 
("MN" , 'MN'),
 
("MO" , 'MO'),
 
("MS" , 'MS'),
 
("MT" , 'MT'),
 
("NC" , 'NC'),
 
("NE" , 'NE'),
 
("NH" , 'NH'),
 
("NJ" , 'NJ'),
 
("NM" , 'NM'),
 
("NV" , 'NV'),
 
("NY" , 'NY'),
 
("ND" , 'ND'),
 
("OH" , 'OH'),
 
("OK" , 'OK'),
 
("OR" , 'OR'),
 
("PA" , 'PA'),
 
("RI" , 'RI'),
 
("SC" , 'SC'),
 
("SD" , 'SD'),
 
("TN" , 'TN'),
 
("TX" , 'TX'),
 
("UT" , 'UT'),
 
("VT" , 'VT'),
 
("VA" , 'VA'),
 
("WA" , 'WA'),
 
("WI" , 'WI'),
 
("WV" , 'WV'),
 
("WY", 'WY'),
]

# Create your models here.
class Data(models.Model):
    year = models.IntegerField()
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    population = models.IntegerField()

    def __unicode__(self):
        return {
            'id': self.id,
            'year': self.year,
            'state': self.state,
            'population': self.population
        }

    def dump(self):
        return {
            'id': self.id,
            'year': self.year,
            'state': self.state,
            'population': self.population
        }