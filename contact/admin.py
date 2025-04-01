from django.contrib import admin
from contact import models



@admin.register(models.contact)
class ContactAdmin(admin.ModelAdmin):
   ...