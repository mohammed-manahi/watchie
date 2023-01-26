from datetime import date, timedelta
from django import forms
from account.models import User, Profile, Subscription


class UserEditForm(forms.ModelForm):
    """
    Create user edit form to edit default user fields
    """
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class LoginForm(forms.Form):
    """
    Create login form to authenticate users
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    """
    Create register form to register new users
    """
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        """
         Set form model and fields required rather than password and repeat password fields
        """
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        """
        Check if password and repeat password fields match and its pattern starts with clean_fieldname
        :return password2:
        """
        data = self.cleaned_data
        if data["password"] != data["password2"]:
            raise forms.ValidationError("Passwords don't match")
        return data["password2"]


class ProfileForm(forms.ModelForm):
    """
    Create profile model form
    """
    photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-primary'}))

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo', 'favorite']
        widgets = {
            'date_of_birth': forms.widgets.DateInput(
                attrs={'type': 'date', 'class': 'form-control flatpickr flatpickr-input form-control active'})}

    def clean_date_of_birth(self):
        """
        Custom validation for date of birth
        :return validated date of birth:
        """
        if self.cleaned_data['date_of_birth'] is not None:
            date_of_birth = self.cleaned_data['date_of_birth']
            age = (date.today() - date_of_birth) // timedelta(days=365.2425)
            if age < 18:
                raise forms.ValidationError("Birthday is not allowed")
            return date_of_birth
        else:
            return None


class SubscriptionForm(forms.ModelForm):
    """
    Create subscription form
    """

    class Meta:
        """
        Registration should add trial subscription (14 days) with generated uuid of subscription code
        """
        model = Subscription
        fields = ['type']
