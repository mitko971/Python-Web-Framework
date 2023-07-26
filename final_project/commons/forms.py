from django import forms

from final_project.commons.models import Contact, Comments
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        label=_('Имe'),
        widget=forms.TextInput(
            attrs={'placeholder': 'Въведете имe'}
        )
    )
    email = forms.EmailField(
        label=_('Имейл'),
        widget=forms.EmailInput(
            attrs={'placeholder': 'Въведете имейл'}
        )
    )
    description = forms.CharField(
        label=_('Описание'),
        widget=forms.Textarea(
            attrs={'placeholder': 'Въведете вашите въпроси:'}
        )
    )

    class Meta:
        model = Contact
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('description',)
