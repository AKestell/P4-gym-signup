from django.contrib import admin
from .models import GymClass, Membership, Booking, Review

# Register your models here.
admin.site.register(GymClass)
admin.site.register(Membership)
admin.site.register(Booking)
admin.site.register(Review)