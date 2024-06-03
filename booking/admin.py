from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import GymClass, Membership, Booking, Review


class BookingAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',) 


admin.site.register(GymClass)
admin.site.register(Membership)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Review)
