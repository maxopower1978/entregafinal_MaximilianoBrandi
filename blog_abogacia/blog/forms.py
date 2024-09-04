from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if 'avatar' in self.cleaned_data:
                Profile.objects.create(user=user, avatar=self.cleaned_data['avatar'])
        return user
