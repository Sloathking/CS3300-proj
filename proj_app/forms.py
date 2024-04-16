from django import forms
from .models import Session
from .widgets import DateInput, TimeInput

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'is_public', 'game', 'date', 'time', 'description']
        widgets = {
            'date': DateInput(),
            'time': TimeInput(format='%H:%M'),
        }
