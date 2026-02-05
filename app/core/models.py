from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class UNASHomePage(Page):
    max_count = 1  # solo 1 página de inicio

    hero_title = models.CharField("Título principal", max_length=120, blank=True)
    hero_subtitle = RichTextField("Subtítulo", blank=True, features=["bold", "italic", "link"])

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
    ]
