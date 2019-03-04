from django.contrib import admin

# Register your models here.
from .models import Sitreps
import datetime

class SitrepsAdmin(admin.ModelAdmin):
    list_display = ['title','modified_custom','pub_date']
    fields=['title','text','modified_custom','pub_date']
    readonly_fields = ['modified_custom']
    #inlines = [ArticleInline]
    search_fields = ['title']

    def modified_custom(self, obj):
        return obj.modified.strftime('%Y-%m-%d %H:%M:%S %Z')

    modified_custom.short_description = 'Modified'

admin.site.register(Sitreps,SitrepsAdmin)