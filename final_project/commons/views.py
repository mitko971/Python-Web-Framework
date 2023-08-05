from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from final_project.commons.forms import ContactForm
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



