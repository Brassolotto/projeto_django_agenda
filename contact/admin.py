from django.contrib import admin
from contact import models



@admin.register(models.contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_date')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    # list_filter = ('created_date',)
    ordering = ('-created_date',)
    list_per_page = 20
    list_max_show_all = 100