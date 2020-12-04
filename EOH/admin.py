from django.contrib import admin
from .models import Node, Performance, NodeToken

# NodeTokenAdmin dependencies
from django.contrib.admin.views.main import ChangeList
from django.core.exceptions import ValidationError
from django.contrib.admin.utils import quote
from django.urls import reverse

# Register your models here.


# custom change list class needed for NodeTokenAdmin
# sourced from default and changed to support node implementation
class NodeTokenChangeList(ChangeList):
    """Map to matching node id"""
    def url_for_result(self, result):
        pk = result.node.pk
        return reverse('admin:%s_%s_change' % (self.opts.app_label,
                                               self.opts.model_name),
                       args=(quote(pk),),
                       current_app=self.model_admin.admin_site.name)

# custom token admin (sourced from TokenAdmin default and
# only altered where necessary for NodeToken implementation)
class NodeTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'node', 'created')
    fields = ('node',)
    ordering = ('-created',)
    actions = None  # Actions not compatible with mapped IDs.

    def get_changelist(self, request, **kwargs):
        return NodeTokenChangeList

    def get_object(self, request, object_id, from_field=None):
        """
        Map from Node ID to matching Token.
        """
        queryset = self.get_queryset(request)
        field = Node._meta.pk
        try:
            object_id = field.to_python(object_id)
            node = Node.objects.get(**{field.name: object_id})
            return queryset.get(node=node)
        except (queryset.model.DoesNotExist, Node.DoesNotExist, ValidationError, ValueError):
            return None

    def delete_model(self, request, obj):
        # Map back to actual Token, since delete() uses pk.
        token = NodeToken.objects.get(key=obj.key)
        return super().delete_model(request, token)


admin.site.register(NodeToken, NodeTokenAdmin)



# EOH nodes
class NodeAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'id')
    list_display = ('name', 'initialized', 'last_update')

admin.site.register(Node, NodeAdmin)



#EOH Node database field for performance logs (cpu, mem, sensors)
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