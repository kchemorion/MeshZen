from django import forms

class MeshSearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=255, required=False)
