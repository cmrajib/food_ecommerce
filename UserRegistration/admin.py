from django.contrib import admin


# Register your models here.
from UserRegistration.models import User, Coupon


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'address_1', 'phone','city')
    list_display_links = ('email', 'full_name')
    # list_filter = ('user__email','full_name','city')
    # list_editable = ('is_featured',)
    search_fields =('full_name', 'phone')
    list_per_page = 10




admin.site.register(User, UserAdmin)
admin.site.register(Coupon)


