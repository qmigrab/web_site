from django.contrib import admin
from .models import CApply


# Register your models here.
@admin.register(CApply)
class CApplyAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'send_time')
	readonly_fields = ('name', 'email', 'content', 'send_time')

	def has_add_permission(self, request):
		return False
