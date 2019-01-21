
from  django import forms
from .models import Slots

CHOICES = (('1', 'RESET'), ('0', 'SAVE'))

class SlotForm( forms.ModelForm ):
    filled_seats_1 = forms.CharField(disabled=True)
    filled_seats_2 = forms.CharField(disabled=True)
    filled_seats_3 = forms.CharField(disabled=True)
    update_choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Slots
        fields = '__all__'
        labels = { 
            'slot_1': '',
            'slot_2': '',
            'slot_3': '',
            'slot_4': '',
            'slot_5': '',
            'slot_6': '',
            'slot_7': '',
            'slot_8': '',
            'slot_9': '',
            'total_seats_1': '',
            'total_seats_2': '',
            'total_seats_3': '',
            'filled_seats_1': 'vacant seats 1',
            'filled_seats_2': 'vacant seats 2',
            'filled_seats_3': 'vacant seats 3',
            'reserved': 'RESERVED SEATS',
            'update_choice': '',
                }
