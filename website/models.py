from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from core.constants import LanguageChoice


class AbstractArticle(models.Model):
    title = models.CharField(max_length=254, unique=True)
    description = models.TextField()

    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(AbstractArticle):
    # this model does not cover the case where default language is changed
    lang = models.CharField(max_length=2, choices=LanguageChoice.CHOICES, default=LanguageChoice.get_default)
    slug = models.SlugField(blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} : {self.lang}"

    def clean(self):
        super().clean()
        if self.lang != LanguageChoice.get_default() and not self.parent:
            raise ValidationError('Add Article in default language first')

        if self.lang == LanguageChoice.get_default() and self.parent:
            raise ValidationError('Article in default language has already been provided')
