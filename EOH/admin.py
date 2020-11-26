from django.contrib import admin
from .models import Node, Performance

# Register your models here.


class NodeAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = ('name', 'ip_address', 'initialized', 'last_update')

admin.site.register(Node, NodeAdmin)


#EOH Node database field for server performance (cpu, mem, sensors)
class PerformanceAdmin(admin.ModelAdmin):
	readonly_fields = (
		'data_columns', 
		'rows', 
		'data_start', 
		'data_end', 
		'initialized', 
		'last_update'
	)

admin.site.register(Performance, PerformanceAdmin)