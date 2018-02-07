from haystack import indexes
from apps.blog.models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # author = indexes.CharField (model_attr='author')
    # created_time = indexes.DateTimeField (model_attr='created_time')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
