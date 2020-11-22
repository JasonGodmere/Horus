from django.contrib import admin




from .models import Snippet
#display the id of each snippet as readonly from admin
class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    #list_display = ('id', 'title', 'code', 'linenos', 'language', 'style')

admin.site.register(Snippet, SnippetAdmin)