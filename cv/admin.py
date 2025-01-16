from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import HomepageText, Hobby, PieChartData


class HomepageTextAdmin(TranslationAdmin):
    list_display = ('title',)


class HobbyAdmin(TranslationAdmin):
    list_display = ('title', 'description')


class PieChartDataAdmin(admin.ModelAdmin):
    list_display = ('label', 'hours', 'color')


admin.site.register(HomepageText, HomepageTextAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(PieChartData, PieChartDataAdmin)
