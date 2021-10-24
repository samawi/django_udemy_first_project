from django.core import validators
from django import forms

# def starts_with_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('NAME MUST START WITH Z')

class FirstForm(forms.Form):
    name = forms.CharField(max_length=254)
    email = forms.EmailField(max_length=254)
    vemail = forms.EmailField(label='Please verify your email address')
    text = forms.CharField(widget=forms.Textarea)
    botcather = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    # def clean_botcather(self):
    #     botcather = self.cleaned_data['botcather']
    #     if len(botcather) > 0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #     return botcather

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        vemail = cleaned_data['vemail']
        if email != vemail:
            raise forms.ValidationError('Both emails must match!')