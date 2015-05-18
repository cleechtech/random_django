from .models import UserProfile
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['hair_color', 'birthdate', 'favorite_hobby', 'created'] # only show these fields
        fields = '__all__' # default behavior
        exclude = ['birthdate',] # don't show these fields