from django.contrib import admin
from .models import Node, Performance

# Register your models here.


class NodeAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = ('name', 'initialized', 'last_update')

admin.site.register(Node, NodeAdmin)


#EOH Node database field for server performance (cpu, mem, sensors)
class PerformanceAdmin(admin.ModelAdmin):
	readonly_fields = (
		'node',
		'data_columns', 
		'rows', 
		'data_start', 
		'data_end', 
		'initialized', 
		'last_update'
	)
	list_display = (
		'node', 
		'initialized', 
		'data_start', 
		'data_end',
		'last_update',
	)


admin.site.register(Performance, PerformanceAdmin)