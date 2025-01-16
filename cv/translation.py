from modeltranslation.translator import translator, TranslationOptions
from .models import Hobby, HomepageText


class HobbyTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class HomepageTextTranslationOptions(TranslationOptions):
    fields = ('content',)


translator.register(Hobby, HobbyTranslationOptions)
translator.register(HomepageText, HomepageTextTranslationOptions)
