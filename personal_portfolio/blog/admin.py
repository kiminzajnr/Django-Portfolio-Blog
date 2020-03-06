from django.contrib import admin
from blog.models import Post, Category
from django.contrib.auth.models import Group

class PostAdmin(admin.ModelAdmin):
	list_display = ('title',)
	list_filter = ('created_on',)

class CategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(Group)

admin.site.site_header = "My Portfolio Administration"

