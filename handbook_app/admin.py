from django.contrib import admin

from .models import Handbook, Element, Version


class HandBookAdmin(admin.ModelAdmin):
    list_display = ['title', 'mini_title', 'description', 'start_date']


class ElementAdmin(admin.ModelAdmin):
    list_display = ['handbook', 'code', 'value']


class VersionAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Handbook, HandBookAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Version, VersionAdmin)
