"""Admin posts"""
# Django
from django.contrib import admin
from django.utils.html import mark_safe
# Models
from posts.models import Post


@admin.register(Post)
class PostsUsers(admin.ModelAdmin):
    list_display = ('title', 'photo', 'user', 'created')
    search_fields = (
        'title', 
        'user__username', 
        'user__email',
        'user__first_name',
        'user__last_name',
    )
    list_filter = ('created', 'modified')

    fieldsets = (
        ('Post Info', {
            'fields': (
              ('title', 'user'),
              ('photo', 'photo_picture')
            ),
        }),
        ('Metadata', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified', 'photo_picture')

    def photo_picture(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="300px"/>')