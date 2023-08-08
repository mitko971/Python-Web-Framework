from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from final_project.hotels.views import UploadHotel, ViewUserHotels, EditHotel, DeleteHotel, ReservationView, \
    InformationView, comment_view, delete_comment, search_view

urlpatterns = [
    path('search/', search_view, name='search'),
    path('upload/', UploadHotel.as_view(), name='upload hotel'),
    path('myhotels/', ViewUserHotels.as_view(), name='my hotel'),
    path('<int:pk>/', include([
        path('information/', InformationView.as_view(), name='information hotel'),
        path('information/comment', comment_view, name='comment'),
        path('information/comment/delete', delete_comment, name='delete comment'),
        path('reservation/', ReservationView.as_view(), name='reservation'),
        path('edit/', EditHotel.as_view(), name='edit hotel'),
        path('delete/', DeleteHotel.as_view(), name='delete hotel'),
    ]))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)