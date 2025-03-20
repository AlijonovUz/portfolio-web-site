from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import *


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'url', 'getPhoto')
    list_display_links = ('id', 'title')
    list_filter = ('id', 'title')
    list_per_page = 10
    search_fields = ('id', 'title')
    actions_on_top = False
    actions_on_bottom = True

    prepopulated_fields = {
        'slug': ('title',)
    }

    def getPhoto(self, data):
        if data.image:
            return mark_safe(f'<img src="{data.image.url}" width="50px">')
        return "—"

    getPhoto.short_description = "Rasmi"


admin.site.register(Technology)
admin.site.register(Comment)
admin.site.register(Portfolio, PortfolioAdmin)
