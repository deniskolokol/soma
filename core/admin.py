from django.contrib import admin

from .models import TaggedItem, ScoredItem, Score

class ScoreAdmin(admin.ModelAdmin):
    list_display = ("name", "minval", "maxval", "user", "privacy", )
    list_filter = ("user", "privacy", )


# XXX display scores of authenticated user (unless SU, then display all)
class ScoredItemAdmin(admin.ModelAdmin):
    list_display = ("score", "val", "content_object", )
    ordering = ("score", "val", "object_id", )
    list_filter = ("score__name", "content_type", )


class TaggedItemAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "content_object", )
    ordering = ("user", "name", "object_id", )
    list_filter = ("user", "content_type", )


admin.site.register(TaggedItem, TaggedItemAdmin)
admin.site.register(ScoredItem, ScoredItemAdmin)
admin.site.register(Score, ScoreAdmin)
