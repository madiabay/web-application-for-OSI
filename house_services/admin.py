from django.contrib import admin

from . import models


class House_serviceImageInline(admin.TabularInline):
    model = models.House_serviceImage
    extra = 1

class House_serviceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    inlines = (House_serviceImageInline,)


admin.site.register(models.House_serviceImage)
admin.site.register(models.House_service, House_serviceAdmin)

