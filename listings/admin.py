from django.contrib import admin
from listings.models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','number','price','created')

admin.site.register(Listing, ListingAdmin)