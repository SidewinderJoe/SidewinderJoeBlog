from django.contrib import admin

# Register your models here.

from . import models

from django.db.models import TextField

class EntryAdmin(admin.ModelAdmin):
	list_display = ("title", 'created', 'publish')
	prepopulated_fields = {"slug": ("title",)}
	list_editable = ('publish',)

admin.site.register(models.Entry, EntryAdmin)