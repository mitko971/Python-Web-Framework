from django import forms

from final_project.hotels.models import Hotels, ReservationModel


# class MultipleImageField(forms.ImageField):
#     def to_python(self, data):
#         if isinstance(data, list):
#             return [super().to_python(item) for item in data]
#         return super().to_python(data)


class HotelForm(forms.ModelForm):
    hotel_name = forms.CharField(
        label='Име на Хотела',
        widget=forms.TextInput(
            attrs={'placeholder': 'Въведете името на хотела'}
        )
    )
    location = forms.CharField(
        label='Локация',
        widget=forms.TextInput(
            attrs={'placeholder': 'Въведете локацията'}
        )
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            attrs={'placeholder': 'Въведете описание'}
        )
    )
    price = forms.CharField(
        label='Цена',
        widget=forms.TextInput(
            attrs={'placeholder': 'Въведете цена за стая за 1 ден'}
        )
    )
    stars = forms.CharField(
        label="Звези на хотела",
        widget=forms.NumberInput(
            attrs={'placeholder': 'Въведете звездите на хотела  (1-5)'}
        )
    )
    hotel_picture = forms.ImageField(
        label='Снимка'
    )

    class Meta:
        model = Hotels
        exclude = ('attached_user', 'reserve_by', 'created_by_user')


class ReservationForm(forms.ModelForm):
    total_price = forms.DecimalField(
        label='',
        widget=forms.NumberInput(
            attrs={'hidden': True, }
        )
    )
    days = forms.IntegerField(
        label='Дни',
        widget=forms.NumberInput(
            attrs={'placeholder': "Въведете нощувки"}
        )
    )

    class Meta:
        model = ReservationModel
        exclude = ('attached_user', 'attached_hotel',)
        labels = {
            'choices': 'Избор'
        }


class EditHotelForm(forms.ModelForm):
    class Meta:
        model = Hotels
        fields = ('hotel_name', 'location', 'description', 'price', 'stars', 'hotel_picture')
        labels = {
            'hotel_name': 'Име на хотела',
            'location': 'Локация',
            'description': 'Описание',
            'price': 'Цена за нощувка',
            'stars': 'Звезди',
            'hotel_picture': 'Снимка на хотела'
        }
