from django.contrib import admin
from .models import  Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug','content', 'status','created_on')
	list_filter = ("status",)
	prepopulated_fields ={'slug':('title',)}

# admin.site.register(Article,ArticleAdmin)