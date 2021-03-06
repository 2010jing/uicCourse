from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from voting.models import Tags
from .models import Notice


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CreateTagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'


class ProfileModifyForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password')


class CreateNoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('title', 'content', 'is_visible')
