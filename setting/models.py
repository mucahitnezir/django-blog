from django.db import models
from django.template.defaultfilters import truncatechars


class Setting(models.Model):
    key = models.CharField(max_length=32, unique=True, verbose_name='Parametre', editable=False)
    description = models.CharField(max_length=255, verbose_name='Parametre Açıklaması', null=True, blank=True)
    value = models.TextField(verbose_name='Parametre Değeri', null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='Son Güncelleme Tarihi', auto_now=True, null=True, blank=True)

    @property
    def admin_list_value(self):
        return truncatechars(self.value, 100)

    class Meta:
        ordering = ['key']
        db_table = 'settings'
        verbose_name = 'Ayar'
        verbose_name_plural = 'Ayarlar'

    def __str__(self):
        return self.key

    @staticmethod
    def get_one(key, return_type='value'):
        # Find setting
        setting = Setting.objects.get(key=key)
        # Return setting
        if return_type == 'value':
            return setting.value
        elif return_type == 'full':
            return setting
        else:
            return None

    @staticmethod
    def get_multiple(keys):
        result = {}
        settings = Setting.objects.filter(key__in=keys)
        for setting in settings:
            result[setting.key] = setting.value
        return result
