from django.contrib import admin
from django.utils.safestring import mark_safe

from slink.core.models import LinkModel
from slink.core.serializers import LinkModelSerializer


class LinkModelAdmin(admin.ModelAdmin):
    fields=('id', 'url', 'short')
    readonly_fields=('id', 'short')
    list_display=('url', 'id', 'short')

    def get_queryset(self, request, *args, **kwargs):
        self.request = request
        return super().get_queryset(request, *args, **kwargs)

    def short(self, obj):
        short_url = LinkModelSerializer(instance=obj, context={'request': self.request}).data['short']
        return mark_safe('<a target="_blank" href="%s">%s</a>' % (short_url, short_url))
    short.short_description = 'Short URL'


admin.site.register(LinkModel, LinkModelAdmin)
