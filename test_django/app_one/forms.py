from django import forms
from app_one import models
class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class':'form-control',
            'placeholder':'Write a post...'
        }
    ))

    class Meta:
        model = models.PostModel
        fields = ('post',)
