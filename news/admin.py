from django.contrib import admin
from news.models import Category, Tag, News
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'slug',
            'content',
            'categories',
            'tags',
            'is_active',
            'author',
            'default_image',
            'media',
            'liked_by',
            'required_login',
        ]

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
    list_display        = ('id', 'display_name', 'slug')
    list_display_links  = ('id', 'display_name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields       = ('name_en', 'name_uz', 'name_ru')
    ordering            = ('name_en', 'name_uz', 'name_ru')

    def display_name(self, obj):
        # Сначала пробуем English, затем Uzbek, затем Russian
        return obj.name_en or obj.name_uz or obj.name_ru
    display_name.short_description = 'Name'



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display        = ('id', 'display_name', 'slug')
    list_display_links  = ('id', 'display_name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields       = ('name_en', 'name_uz', 'name_ru')
    ordering            = ('name_en', 'name_uz', 'name_ru')

    def display_name(self, obj):
        return obj.name_en or obj.name_uz or obj.name_ru
    display_name.short_description = 'Name'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    fieldsets = (
        (_("Main"), {
            'fields': ('title', 'slug', 'is_active', 'required_login', 'author', 'default_image'),
        }),
        (_("English"), {
            'fields': ('title_en', 'content_en'),
        }),
        (_("Uzbek"), {
            'fields': ('title_uz', 'content_uz'),
        }),
        (_("Russian"), {
            'fields': ('title_ru', 'content_ru'),
        }),
        (_("Relations"), {
            'fields': ('categories', 'tags', 'media', 'liked_by'),
        }),
    )
    list_display        = (
        'id', 'title', 'slug', 'author',
        'required_login', 'like_count',
        'created_at', 'updated_at',
        'is_active',
    )
    list_display_links  = ('id', 'title', 'slug')
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
        'like_count',
        'created_at',
        'updated_at',
    )
    date_hierarchy      = 'created_at'
    ordering            = ('-created_at',)