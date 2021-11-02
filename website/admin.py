from django.contrib import admin
from .models import UserProfile,Reservation

# Register your models here.
admin.site.register(UserProfile)
#admin.site.register(Reservation)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = ('user_id','id','name')
	ordering = ('user_id','id')