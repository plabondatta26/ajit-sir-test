from django import forms
from .models import *


class WriterForm(forms.ModelForm):
    class Meta:
        model = WriterModel
        fields = '__all__'


