from django import forms
from .models import License

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ['name', 'pdf']



from .models import UserInput

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['phone_number', 'information']
        widgets = {
            'phone_number': forms.TextInput(),
            'information': forms.TextInput(),
        }
