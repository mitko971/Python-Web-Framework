from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView

from final_project.commons.forms import CommentForm
from final_project.commons.models import Comments
from final_project.hotels.forms import HotelForm, ReservationForm, EditHotelForm
from final_project.hotels.models import Hotels, ReservationModel
from django.db import transaction

# Create your views here.

User = get_user_model()


class InformationView(ListView):
    template_name = 'hotels/hotel-information.html'
    model = Hotels

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hotel_pk = self.kwargs.get('pk')

        context['hotel'] = Hotels.objects.get(pk=hotel_pk)
        context['comment_form'] = CommentForm()
        context['comments'] = Comments.objects.filter(hotel=hotel_pk)

        return context


class ViewUserHotels(LoginRequiredMixin, ListView):
    template_name = 'hotels/../../templates/account/user-hotels.html'
    model = Hotels

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotels.objects.filter(created_by_user=self.request.user)

        return context


class UploadHotel(LoginRequiredMixin, CreateView):
    template_name = 'hotels/upload-hotel.html'
    form_class = HotelForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        hotel = form.save(commit=False)
        hotel.created_by_user = self.request.user
        hotel.save()
        return super().form_valid(form)


class ReservationView(LoginRequiredMixin, CreateView):
    template_name = 'common/reservation.html'
    model = ReservationModel
    form_class = ReservationForm
    success_url = reverse_lazy('show all hotels')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hotel_id = self.kwargs['pk']
        context['hotel'] = Hotels.objects.get(id=hotel_id)

        return context

    @transaction.atomic
    def form_valid(self, form):
        reservation = form.save(commit=False)
        reservation.attached_user = self.request.user

        context = self.get_context_data()

        hotel_id = self.kwargs['pk']
        hotel = Hotels.objects.get(id=hotel_id)
        hotel.reserve_by_id = self.request.user.id
        hotel.save()

        reservation.attached_hotel = context['hotel']
        reservation.total_price = form.cleaned_data['total_price']
        reservation.save()

        return super().form_valid(form)


class EditHotel(LoginRequiredMixin, UpdateView):
    model = Hotels
    form_class = EditHotelForm
    template_name = 'hotels/edit-hotel.html'
    success_url = reverse_lazy('my hotel')


class DeleteHotel(LoginRequiredMixin, DeleteView):
    model = Hotels
    template_name = 'hotels/delete-hotel.html'
    success_url = reverse_lazy('home page')
