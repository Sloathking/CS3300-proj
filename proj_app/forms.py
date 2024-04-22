from django import forms
from .models import Session
from .widgets import DateInput, TimeInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'game_name', 'thumbnail' , 'date', 'time', 'description']
        widgets = {
            'game_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'thumbnail': forms.TextInput(attrs={'readonly': 'readonly'}),
            'date': DateInput(),
            'time': TimeInput(format='%H:%M'),
        }

class GameSelectForm(forms.Form):
    game_choices = forms.ChoiceField(label='Select a game', choices=[])

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
