from django.contrib import admin
from accounts.models import UserProfile



# Change the site header from Django Administration to Administration
# admin.site.site_header = "Administration"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description

    # Ordering by Phone Number
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('phone')
        # queryset = queryset.order_by('-phone')

        # Order By more than one field
        # queryset = queryset.order_by('-phone', 'user')
        return queryset
    user_info.short_description = 'Info'

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
