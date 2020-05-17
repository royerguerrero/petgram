"""User admin class"""
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Models
from users.models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""

    list_display = ('id', 'user', 'phone_number', 'website')
    list_display_links = ('id', 'user')
    list_editable = ('phone_number',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('created', 'modified')

    fieldsets = (
        ('Profile',{
            'fields': (('user', 'picture'),),
        }),
        ('Extra info',{
            'fields': (
                ('website', 'phone_number'),
                'biography'
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            ),
        }),
    )

    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    varbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
