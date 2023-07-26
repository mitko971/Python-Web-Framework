from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import views as auth_views, login, get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.views.generic import DetailView, UpdateView, DeleteView, ListView
from final_project.account.forms import CustomRegisterForm, CustomLoginView, EditUserForm
from final_project.commons.models import Comments
from final_project.hotels.forms import ReservationForm
from final_project.hotels.models import Hotels, ReservationModel

# Create your views here.
ModelUser = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'account/register-account.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    success_url = reverse_lazy('home page')
    form_class = CustomLoginView
    template_name = 'account/login_page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = ModelUser
    template_name = 'account/profile-details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = len(ReservationModel.objects.filter(attached_user_id=self.request.user))
        reservation = ReservationModel.objects.filter(attached_user=self.request.user)
        context['price'] = sum(reservation.total_price for reservation in reservation)
        return context


class UserReservation(ListView):
    template_name = 'account/user_reservation.html'
    model = ReservationModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservation'] = ReservationModel.objects.filter(attached_user_id=self.request.user)

        return context


class UserReservationChange(LoginRequiredMixin, UpdateView):
    form_class = ReservationForm
    template_name = 'account/user_reservation_change.html'
    model = ReservationModel

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ReservationModel, pk=pk)

    def get_success_url(self):
        return self.object.get_absolute_url()


class UserDeleteReservation(LoginRequiredMixin, DeleteView):
    model = ReservationModel
    template_name = 'account/user_delete_reservation.html'

    def form_valid(self, form):
        reservation = self.kwargs['pk']

        current_reservation = ReservationModel.objects.filter(pk=reservation).first()
        hotel = current_reservation.attached_hotel
        current_hotel = Hotels.objects.filter(pk=hotel.pk).first()
        current_hotel.reserve_by_id = None

        current_hotel.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(ReservationModel, pk=self.kwargs['pk'])

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = EditUserForm
    template_name = 'account/edit-profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = ModelUser
    template_name = 'account/delete-profile.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        user = self.request.user
        comments = Comments.objects.filter(user=user)
        comments.delete()
        reservations = ReservationModel.objects.filter(attached_user=user)
        reservations.delete()

        return super().form_valid(form)
