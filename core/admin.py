from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Cluster, Node

admin.site.register(User, UserAdmin)
admin.site.register(Profile)


class ClusterAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_on', 'last_update')

admin.site.register(Cluster, ClusterAdmin)


class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'cluster', 'initialized', 'last_update')

admin.site.register(Node, NodeAdmin)