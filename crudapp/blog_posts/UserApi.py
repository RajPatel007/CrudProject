from django import forms
from .models import UserApis


class UserApiForms(forms.ModelForm):
    class Meta:
        model = UserApis
        fields = '__all__'
