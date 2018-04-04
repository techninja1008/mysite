from django.contrib import admin
from .models import Content, Link



class AboutAdmin(admin.ModelAdmin):
    fields = ['heading_text', 'body_text']

    list_display = ('heading_text', )
    search_fields = ['heading_text', 'body_text']

    
class LinkAdmin(admin.ModelAdmin):
    fields = ['link_website', 'link_text', 'link_href']
    list_display = ('link_website', 'link_href')
    search_fields = ['link_website', 'link_href']
    extra = 3

admin.site.register(Link, LinkAdmin)
admin.site.register(Content, AboutAdmin)
