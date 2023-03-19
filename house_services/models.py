from django.db import models
from django.utils.translation import gettext_lazy as _

from . import choices


class House_service(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'), unique=True)
    description = models.TextField(verbose_name=_('description'))
    main_image = models.ImageField(upload_to='house_services/%Y/%m/%d/', verbose_name=_('main_image'))
    is_active = models.BooleanField(default=True, verbose_name=_('is active?'))
    data = models.JSONField(default=dict, verbose_name=_('data'), null=True, blank=True)

    status = models.CharField(
        max_length=50,
        choices=choices.NoteTypeChoices.choices,
        default=choices.NoteTypeChoices.New
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('House_service')
        verbose_name_plural = _('House_services')


class House_serviceImage(models.Model):
    house_service = models.ForeignKey(
        to=House_service, 
        on_delete=models.CASCADE, 
        related_name='house_service_images',
        verbose_name=_('house_service')
    )
    image = models.ImageField(upload_to='house_services_images/%Y/%m/%d/', verbose_name=_('image'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('House_service Image')
        verbose_name_plural = _('House_service Images')
