from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from common.models import BaseModel

User = get_user_model()

class Category(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    slug        = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("tags")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class News(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name='news', blank=True)
    tags = models.ManyToManyField(Tag, related_name='news', blank=True)
    is_active = models.BooleanField(default=True, help_text=_("If false, the news will not be displayed on the site"))
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news',
        null=False,
        blank=False,
    )
    default_image = models.ImageField(upload_to='news_images', null=True, blank=True)
    media = models.ManyToManyField(
        'common.MediaFile',
        related_name='news_media',
        blank=True
    )

    # Новое поле: если заполнено, новость будет опубликована в указанное время
    scheduled_time  = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_("If set, news will be published at this time")
    )
    
    liked_by     = models.ManyToManyField(
        User,
        related_name='liked_news',
        blank=True
    )
    required_login  = models.BooleanField(
        default=False,
        help_text=_("If true, only authenticated users can view this news item")
    )


    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def like_count(self):
        return self.liked_by.count()

    def __str__(self):
        return self.title
    
    