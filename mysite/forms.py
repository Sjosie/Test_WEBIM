from django import forms

class CustomSignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': _('First name')}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': _('Last name')}))

    GENDERS = (('man, _('Man')), ('woman', _('Woman')))
    gender = forms.ChoiceField(label=_('Gender'), choices=GENDERS, widget=forms.Select())

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.gender = self.cleaned_data['gender']

        user.save()