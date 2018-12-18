from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from main_page.models import User


class MyAuthenticationForm(AuthenticationForm):

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )
        if not user.is_verified:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')


    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )
