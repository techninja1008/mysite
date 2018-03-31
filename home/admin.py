from django.contrib import admin
from .models import Content, Page, Link


class ContentInLine(admin.StackedInline):
    model = Content
    extra = 1

class ContentAdmin(admin.ModelAdmin):
    fields = ['page', 'heading_text', 'body_text']

    list_display = ('page', 'heading_text')
    search_fields = ['page', 'heading_text', 'body_text']

    
class PageAdmin(admin.ModelAdmin):
    fields = ['page']
    inlines = [ContentInLine]

class LinkAdmin(admin.ModelAdmin):
    fields = ['link_website', 'link_text', 'link_href']
    list_display = ('link_website', 'link_href')
    search_fields = ['link_website', 'link_href']
    extra = 3

admin.site.register(Link, LinkAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Content, ContentAdmin)
