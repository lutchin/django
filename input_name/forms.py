from django import forms

class NameForm(forms.Form):

    name = forms.CharField(label=False, max_length=20)