from django.contrib import admin

from .models import Asana, AsanaForm
from core.utils import admin_method_attrs, shorten_string


class AsanaAdmin(admin.ModelAdmin):
    @admin_method_attrs(admin_order_field='body')
    def _note(self, obj):
        return shorten_string(obj.note, 80)

    list_display = ("name", "_note", "created", "updated", )
    ordering = ("name", "updated", )
    list_filter = ("updated", )
    search_fields = ("name", "note", )


class AsanaFormAdmin(admin.ModelAdmin):
    @admin_method_attrs(short_description='name',
                        admin_order_field='asana__name')
    def _name(self, obj):
        return obj.name

    @admin_method_attrs(short_description='pict')
    def _pict(self, obj):
        return obj.pict_100x100

    list_display = ("_pict", "_name", )
    ordering = ("asana__name", )
    search_fields = ("asana__name", )


admin.site.register(Asana, AsanaAdmin)
admin.site.register(AsanaForm, AsanaFormAdmin)
