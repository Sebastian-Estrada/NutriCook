
from django import forms


from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label="Email address", max_length=100,
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'id': 'usernameInput',
            'placeholder': 'Email address',
            'class': 'form-control'
        }))
    password = forms.CharField(label="Password", max_length=100,
        widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'type': 'password',
        'id': 'passwordInput',
        'placeholder': 'Password',
            'class': 'form-control'
        }))


class ModifyUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

        self.fields['first_name'].label = _("Nombres")
        self.fields['last_name'].label = _("Apellidos")

    def clean(self):
        form_data = self.cleaned_data
        try:
            user = User.objects.get(email=form_data["email"])
            current_user = self.instance
            if (
                current_user
                and current_user != user
                or not current_user
            ):
                self._errors["email"] = ["The email address already exists"]
        except User.DoesNotExist:
            pass


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'placeholder': 'Password',
            'data-parsley-password': '',
            'class': 'form-control'
        }))

    password2 = forms.CharField(label='Confirm Password', max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'placeholder': 'Confirm Password',
            'data-parsley-confirmation': 'id_password1',
            'class': 'form-control'
        }))

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['password1'].label = "New Password"
        self.fields['password2'].label = "Confirm New Password"

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.strip().title()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.strip().title()

    def clean(self):
        form_data = self.cleaned_data
        try:
            found_user = User.objects.get(email=form_data["email"])
            current_user = self.instance
            if (
                current_user
                and current_user != found_user
                or not current_user
            ):
                self._errors["email"] = ["The email address already exists"]
        except User.DoesNotExist:
            pass


class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(
        label='New Password', max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'placeholder': 'Password',
            'data-parsley-password': '',
            'class': 'form-control'
        }))

    password2 = forms.CharField(label='Confirm New Password', max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'password',
            'placeholder': 'Confirm Password',
            'data-parsley-confirmation': 'id_password1',
            'class': 'form-control'
        }))

    def clean(self):
        form_data = self.cleaned_data
        if form_data["password1"] != form_data["password2"]:
            self._errors["password2"] = ["Passwords do not match"]
        return form_data
