from django.contrib import admin
from .models import UserProfile,Reservation

# Register your models here.
#admin.site.register(UserProfile)
#admin.site.register(Reservation)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = ('user_id','id','name')
	ordering = ('user_id','id')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user_id','id','phone_number','paid','can_change')
	ordering = ('user_id','id')