from django.contrib import admin
from models import CConfig

# Register your models here.
@admin.register(CConfig)
class CConfigAdmin(admin.ModelAdmin):
	list_display = ('site', 'address', 'phone')

	def has_add_permission(self, request):
		return False
