from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import Comment, CommentReply
from main.models import Manga, Chapter

class ContentTypeFilter(admin.SimpleListFilter):
    title = 'Content Type'
    parameter_name = 'content_type'

    def lookups(self, request, model_admin):
        content_types = ContentType.objects.filter(app_label='main')
        return [(ct.id, ct.model_class().__name__) for ct in content_types if ct.model in ['manga', 'chapter']]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(content_type_id=self.value())

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'content_type', 'object_id', 'created_at']
    list_filter = [ContentTypeFilter]

admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentReply)
