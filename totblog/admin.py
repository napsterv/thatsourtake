from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Post, Page, Category, Advertisement
# Register your models here.

# Registering the 4 models on admin panel
#@admin.register(Post, Page, Category, Advertisement)

# customizing admin page for posts


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
# customizing admin page for pages


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Page, PageAdmin)

# customizing admin page for categories


class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CatAdmin)

'''class Advertisement(admin.ModelAdmin):
    pass'''
admin.site.register(Advertisement)

'''class CustomAdminSite(AdminSite):
    site_header = 'thatsourtake.com'
    site_title = 'thatsourtake admin panel'
    index_title = 'Administrator Panel'

totadmin = CustomAdminSite(name='customadmin')

totadmin.register(Categories)
totadmin.register(Post)
totadmin.register(Page)'''
