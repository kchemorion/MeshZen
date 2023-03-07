from django import forms

class MeshSearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label="Search term")
