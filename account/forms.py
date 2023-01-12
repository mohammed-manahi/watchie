from datetime import date, timedelta
from django import forms
from account.models import User, Profile, Subscription


class UserEditForm(forms.ModelForm):
    """
    Create user edit form to edit default user fields
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name"]


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

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo', 'favorite']
        widgets = {'date_of_birth': forms.widgets.DateInput(attrs={'type': 'date'})}

    def clean_date_of_birth(self):
        """
        Custom validation for date of birth
        :return validated date of birth:
        """
        date_of_birth = self.cleaned_data['date_of_birth']
        start_date_range = date(1950, 1, 1)
        end_date_range = date.today() - timedelta(days=6570)
        query_set = Profile.objects.filter(date_of_birth__gte=start_date_range,
                                           date_of_birth__lte=end_date_range)
        if not query_set:
            raise forms.ValidationError("Birthday is not allowed")
        else:
            return date_of_birth


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
