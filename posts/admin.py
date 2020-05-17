"""Posts Admin"""
# Django
from django.contrib import admin
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
              'photo'  
            ),
        }),
        ('Metadata', {
            'fields': ('created', 'modified'),
        }),
    )

    readonly_fields = ('created', 'modified')
    