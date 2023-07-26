from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from final_project.commons.forms import ContactForm, CommentForm
from final_project.hotels.models import Hotels


# Create your views here.
class HotelsView(ListView):
    template_name = 'hotels/all-hotels.html'
    model = Hotels


class HomePageView(auth_views.TemplateView):
    template_name = 'common/home-page.html'


class AboutUsView(auth_views.TemplateView):
    template_name = 'common/about-us.html'


class ContactPage(CreateView):
    form_class = ContactForm
    template_name = 'common/contacts.html'
    success_url = reverse_lazy('home page')



def comment_view(request, pk):
    hotels_pk = Hotels.objects.get(pk=pk)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.hotel = hotels_pk
            comment.user = user
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{hotels_pk}")
