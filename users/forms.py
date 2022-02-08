from django.contrib.auth import forms import
from django.contrib.auth import get_user_model


User = get_user_model()


class CreationForm(forms.UserCreationForm):
    email = forms.Email
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'avatar'
        )


class UserUpdateForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'avatar'
        )
