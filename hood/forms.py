from django import forms
from .models import Profile, Business

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']        