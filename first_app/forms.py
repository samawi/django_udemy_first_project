from django import forms

class FirstForm(forms.Form):
    name = forms.CharField(max_length=254)
    email = forms.EmailField(max_length=254)
    text = forms.CharField(widget=forms.Textarea)