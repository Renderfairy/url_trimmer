from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    """
    Form based on :model: `users.CustomUser`
    """
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email'
    }))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')

    def clean_password2(self):
        """Cleans and validates form password data.
        """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Passwords don`t match')

        return password2

    def save(self, commit=True):
        """ Saves user instance to database.
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field_name in ['username']:
            self.fields[field_name].help_text = None


class LoginForm(AuthenticationForm):
    """Authenticates user.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('username', 'password')
