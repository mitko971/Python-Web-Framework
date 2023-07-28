from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from final_project.commons.views import HomePageView, ContactPage, HotelsView, AboutUsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home page'),
    path('hotels/', HotelsView.as_view(), name='show all hotels'),
    path('contact/', ContactPage.as_view(), name='contact page'),
    path('about-us/', AboutUsView.as_view(), name='about use')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
