
from django.contrib import admin
from .models import User, Tag, Page, Post

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'title', 'role')
    list_display_links = ('email', 'title')
    search_fields = ('email', 'title')
    list_filter = ('email', 'title')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'description',)
    search_fields = ('name', 'owner', 'description',)
    list_filter = ('name', 'owner', 'description',)


admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Page, PageAdmin)
