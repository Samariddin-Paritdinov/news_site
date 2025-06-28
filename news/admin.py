from django.contrib import admin
from news.models import Category, Tag, News
from django import forms
from django.core.exceptions import ValidationError

class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        categories = cleaned_data.get('categories')
        tags       = cleaned_data.get('tags')

        if not categories or categories.count() == 0:
            raise ValidationError("Kamida bitta kategoriya tanlanishi shart")
        if not tags or tags.count() == 0:
            raise ValidationError("Kamida bitta teg tanlanishi shart")

        return cleaned_data


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display         = ('name', 'slug')
    prepopulated_fields  = {'slug': ('name',)}
    search_fields        = ('name',)
    ordering             = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display         = ('name', 'slug')
    prepopulated_fields  = {'slug': ('name',)}
    search_fields        = ('name',)
    ordering             = ('name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display        = (
        'title', 'slug', 'author',
        'required_login', 'like_count',
        'created_at', 'updated_at',
        'is_active',
    )
    list_filter         = (
        'author',
        'categories',
        'tags',
        'is_active',
    )
    search_fields       = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal   = (
        'categories',
        'tags',
        'media',
        'liked_by',
    )
    raw_id_fields       = ('author', 'media')
    readonly_fields     = (
        'required_login',
        'like_count',
        'created_at',
        'updated_at',
    )
    date_hierarchy      = 'created_at'
    ordering            = ('-created_at',)