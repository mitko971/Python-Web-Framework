from django.contrib import admin

from final_project.hotels.models import Hotels


# Register your models here.

@admin.register(Hotels)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'location', 'price', 'stars', 'created_by_user')
    list_filter = ('location', 'stars')
    search_fields = ('hotel_name', 'location')
    ordering = ('-stars',)

    def custom_user_info(self, obj):
        if obj.attached_user:
            return f'{obj.attached_user.first_name} {obj.attached_user.last_name} ({obj.attached_user.email})'
        return '-'

    custom_user_info.short_description = 'Потребител'

