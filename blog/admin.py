from django.contrib import admin

# Register your models here.

from .models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    # 显示模型的列表展示信息。
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


class CategoryAdmin(admin.ModelAdmin):
    # 显示模型的列表展示信息。
    list_display = ['name']


class TagAdmin(admin.ModelAdmin):
    # 显示模型的列表展示信息。
    list_display = ['name']

# 把新增的 PostAdmin 也注册进来
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,CategoryAdmin)







from markdownx.admin import MarkdownxModelAdmin
from .models import MyModel


admin.site.register(MyModel, MarkdownxModelAdmin)

