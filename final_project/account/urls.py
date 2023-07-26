from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import user_passes_test
from django.urls import path, include

from final_project.account.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileDetailsView, \
    ProfileEditView, ProfileDeleteView, UserReservation, UserReservationChange, UserDeleteReservation


def user_not_logged_in(user):
    return not user.is_authenticated


urlpatterns = [
    path('register/', user_passes_test(user_not_logged_in, login_url='/')(RegisterUserView.as_view()), name='sign on'),
    path('login/', user_passes_test(user_not_logged_in, login_url='/')(LoginUserView.as_view()), name='sign in'),
    path('logout/', LogoutUserView.as_view(), name='sign out'),
    path('<int:pk>/', include([
        path('user-reservation/', UserReservation.as_view(), name='user reservation'),
        path('change-reservation/', UserReservationChange.as_view(), name='change reservation'),
        path('delete-reservation/', UserDeleteReservation.as_view(), name='delete reservation'),
        path('details/', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile delete'),
    ]))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
