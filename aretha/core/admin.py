from django.contrib import admin

from core.models import Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_at',
                    'last_modified', 'is_published')
    list_filter = ('is_published', )

admin.site.register(Publication, PublicationAdmin)
