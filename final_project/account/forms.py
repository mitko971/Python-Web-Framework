from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _

from final_project.account.models import Profile, CustomRegisterUser

UserModel = get_user_model()


class CustomRegisterForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'profile_picture')

    def save(self, commit=True):
        user = super().save(commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user,
        )
        if commit:
            profile.save()

        return user

    email = forms.EmailField(
        label=_('Имейл'),
        widget=forms.EmailInput(
            attrs={'placeholder': 'Въведете имейл'}
        )
    )
    first_name = forms.CharField(
        label=_('Име'),
        widget=forms.TextInput(
            attrs={'placeholder': 'Въведете име'}
        )
    )
    last_name = forms.CharField(
        label=_('Фамилия'),
        widget=forms.TextInput(
            attrs={'placeholder': 'Въведете фамилия'}
        )
    )
    profile_picture = forms.ImageField(
        label=_('Профилна снимка'),
        required=False,
    )

    password1 = forms.CharField(
        label=_('Парола'),
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Въведете парола'}
        )
    )
    password2 = forms.CharField(
        label=_("Потвърдете паролата"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          'placeholder': 'Повторете паролата'}),

    )


class CustomLoginView(auth_forms.AuthenticationForm):
    username = UsernameField(
        label=_('Имейл'),
        widget=forms.TextInput(
            attrs={"autofocus": True,
                   'placeholder': 'Въведете имейл'
                   }
        )
    )
    password = forms.CharField(
        label=_('Парола'),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'placeholder': 'Въведете парола'}),
    )

    error_messages = {
        "invalid_login": _(
            "Моля, въведете правилно имейл и парола."
        ),
        "inactive": _("This account is inactive."),
    }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomRegisterUser
        fields = ('email', 'first_name', 'last_name', 'profile_picture',)
        labels = {
            'email': 'Имейл',
            'first_name': 'Име',
            'last_name': 'Фамилия',
            'profile_picture': 'Профилна снимка',
        }
