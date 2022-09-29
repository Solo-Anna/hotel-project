
from django import forms
from .models import Hotel, Location, Country, Order

class SearchByCountry (forms.Form):
    CHOICES= [(choice.countryId, choice.countryName) for choice in Country.objects.all()]
    query = forms.ChoiceField(choices=CHOICES, required = False, widget=forms.Select, label='Направление')

class SendOrder2 (forms.ModelForm):
    class Meta:
        model = Order
        fields = ('checkIn', 'checkOut', 'adults', 'children', 'name', 'phone_number')
        

class SendOrder (forms.Form):
    ADULTS = [('1','1'), ('2','2') , ('3','3'), ('4','4')]
    CHILDREN = [('0','0'), ('1','1'),('2','2' ), ('3','3'), ('4', '4')]
    checkIn = forms.DateField (required = True, widget=forms.SelectDateWidget)
    checkOut = forms.DateField (required = True, widget=forms.SelectDateWidget)
    adults = forms.ChoiceField(required = False, widget=forms.Select, choices=ADULTS)
    children = forms.ChoiceField(required = False, widget=forms.Select, choices=CHILDREN)
    name = forms.CharField(max_length=30)
    phone_number = forms.CharField(max_length=13)