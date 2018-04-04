from django.contrib import admin
from .models import Details


class HomeAdmin(admin.ModelAdmin):
    fields = ['welcome_msg']
admin.site.register(Details, HomeAdmin)
