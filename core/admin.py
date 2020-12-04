from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Cluster


admin.site.register(User, UserAdmin)
admin.site.register(Profile)


class ClusterAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_on', 'last_update')

admin.site.register(Cluster, ClusterAdmin)