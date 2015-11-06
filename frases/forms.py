from django import forms
from .models import Frase

class PostForm(forms.ModelForm):

    class Meta:
        model = Frase
        fields = ('personaje', 'categoria', 'texto',)
