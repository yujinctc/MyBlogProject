# 自定义模板代码写在blog_tags中，这是标准命名吗？

from django import template
from django.db.models import Count

from blog.models import Article, Category, Tag

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_all_user_archives(num=24):
    return Article.objects.dates ('created_time', 'month', order='DESC')[:num]



@register.simple_tag(takes_context=True)
def get_archives(context,num=24):
    try:
        user=context['user']

        return Article.objects.filter(author=user).dates ('created_time', 'month', order='DESC')[:num]

    except Exception :
        pass
    return Article.objects.dates ('created_time', 'month', order='DESC')[:num]

# @register.simple_tag
# def get_categories():
#     # 别忘了在顶部引入 Category 类
#     return Category.objects.all()


@register.simple_tag(takes_context=True)
def get_most_popular_categories(context,num=10):
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0).order_by('-num_posts')[:num]

@register.simple_tag(takes_context=True)
def get_categories(context,num=10):
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    try:
        user=context['user']
        user = context['user']
        return Category.objects.filter(article__author=user).annotate(num_posts=Count('article')).filter(num_posts__gt=0)[:num]

    except Exception :
        pass
    return Category.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)[:num]



@register.simple_tag(takes_context=True)
def get_tags(context,num=10):
    # 记得在顶部引入 Tag model
    try:
        user=context['user']

        return Tag.objects.filter(article__author=user).annotate(num_posts=Count('article')).filter(num_posts__gt=0)[:num]

    except Exception :
        pass
    return Tag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)[:num]