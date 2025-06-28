from modeltranslation.translator import register, TranslationOptions
from .models import News, Category, Tag

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name', )