from django.contrib.syndication.views import Feed

from .models import Article


class ArticleRssFeed(Feed):
    """这是个Feed子类，用于实现rss功能"""
    # 显示在聚合阅读器上的标题
    title = "一个演示"

    # 通过聚合阅读器跳转到网站的地址
    link = "/"

    # 显示在聚合阅读器上的描述信息
    description = "RSS测试内容"

    # 需要显示的内容条目
    @staticmethod
    def items():
        return Article.objects.all()[:5]

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.excerpt
