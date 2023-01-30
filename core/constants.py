from django.db import models
from django.utils.translation import gettext as _


class LanguageChoice:
    ENGLISH = _('en')
    HINDI = _('hi')

    CHOICES = (
        (ENGLISH, ENGLISH),
        (HINDI, HINDI),
    )

    @staticmethod
    def get_default():
        return LanguageChoice.ENGLISH

    @staticmethod
    def get_enabled_languages():
        return [LanguageChoice.ENGLISH,
                LanguageChoice.HINDI
                ]
