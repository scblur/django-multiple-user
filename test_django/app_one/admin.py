from django.contrib import admin
from app_one import models
from app_one.models import PostModel, FriendModel

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated' ,'post')

    def user_info(self, obj):
        return obj.post

    # Ordering by Phone Number
    def get_queryset(self, request):
        queryset = super(PostModelAdmin, self).get_queryset(request)
        queryset = queryset.order_by('updated')
        # queryset = queryset.order_by('-phone')

        # Order By more than one field
        # queryset = queryset.order_by('-phone', 'user')
        return queryset
    # user_info.short_description = 'Info'

# Register your models here.
admin.site.register(models.PostModel, PostModelAdmin)
admin.site.register(FriendModel)
