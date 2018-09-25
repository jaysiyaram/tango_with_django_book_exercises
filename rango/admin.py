from django.contrib import admin

# Register your models here.
from rango.models import Category, Page, UserProfile


#class PageAdmin(admin.ModelAdmin):
#    list_display = ('title', 'category', 'url')
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# admin.site.register(PageAdmin)
admin.site.register(Category)
# admin.site.register(Page, PageAdmin)
admin.site.register(Page)

admin.site.register(UserProfile)
