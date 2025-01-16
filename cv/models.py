from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _


class HomepageText(models.Model):
    content = HTMLField(_("Homepage Content"))
    title = models.CharField(_("Title"), max_length=50, default="Title")

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")

    def __str__(self):
        return self.title


class Hobby(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"))
    image = models.ImageField(upload_to='hobby_images/')

    class Meta:
        verbose_name = _("Hobby")
        verbose_name_plural = _("Hobbies")

    def __str__(self):
        return self.title


class PieChartData(models.Model):
    label = models.CharField(_("Label"), max_length=100)
    hours = models.IntegerField(_("Hours"))
    color = models.CharField(_("Color"), max_length=20)

    class Meta:
        verbose_name = ("Experience")
        verbose_name_plural = ("Experiences")

    def __str__(self):
        return self.label
