from django.db import models
from django.urls import reverse


class Countries(models.Model):
    country_id = models.IntegerField(
        default=90, null=True, blank=True, verbose_name='ID')
    country_name = models.CharField(
        max_length=20, null=True, blank=True,  verbose_name='Name')
    country_logo = models.URLField(
        default='EMPTY', blank=True,  verbose_name='Logo')

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.country_name

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
