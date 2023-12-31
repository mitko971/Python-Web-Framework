from django.contrib import admin

from final_project.commons.models import Contact, Comments


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'description')
    list_filter = ('email',)
    search_fields = ('first_name', 'email')
    ordering = ('first_name', 'email')


@admin.register(Comments)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'user', 'description', 'hotel')
    list_filter = ('hotel',)
    search_fields = ('user',)
    ordering = ('user', )
