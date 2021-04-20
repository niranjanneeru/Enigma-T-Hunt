from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['name', 'college', 'nick_name', 'marks']
    list_display = ['name', 'marks', 'college']
    list_filter = ['marks']


admin.site.register(Profile, ProfileAdmin)
