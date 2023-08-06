from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('final_project.commons.urls')),
    path('account/', include('final_project.account.urls')),
    path('hotels/', include('final_project.hotels.urls')),
]
