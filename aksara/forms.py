from .models import Aksara
from django import forms
class AksaraForm(forms.ModelForm):
    class Meta:
        model = Aksara
        fields = ['gambar']