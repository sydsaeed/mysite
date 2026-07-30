from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','massage')
    date_hierarchy = 'created_date'

admin.site.register(Contact, ContactAdmin)
