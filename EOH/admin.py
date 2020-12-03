from django.contrib import admin
from .models import Node, Performance

# Register your models here.


class NodeAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'id')
    list_display = ('name', 'initialized', 'last_update')

admin.site.register(Node, NodeAdmin)


#EOH Node database field for server performance (cpu, mem, sensors)
class PerformanceAdmin(admin.ModelAdmin):
	readonly_fields = (
		'general_columns',
		'general_data',
		'cpu_columns',
		'cpu_data',
		'gpu_columns', 
		'gpu_data',
		'rows', 
		'data_start', 
		'data_end', 
		'created', 
		'last_update'
	)
	list_display = (
		'node', 
		'created', 
		'data_start', 
		'data_end',
		'last_update',
	)


admin.site.register(Performance, PerformanceAdmin)