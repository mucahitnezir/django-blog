from django.db import models
from django.utils.translation import ugettext_lazy as _


class TeamMember(models.Model):
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    title = models.CharField(_('Degree'), max_length=100)
    email = models.EmailField(_('Email Address'))
    linkedin_url = models.URLField(_('Linkedin Address'), null=True, blank=True)
    image = models.ImageField(_('Profile Photo'), null=True, blank=True)
    published_at = models.DateTimeField(_('Publishing Date'), auto_now_add=True, editable=False)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        db_table = 'team_members'
        ordering = ('id',)
        verbose_name = _('Team Member')
        verbose_name_plural = _('Team Members')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Message(models.Model):
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    email_address = models.EmailField(_('Email Address'))
    subject = models.CharField(_('Subject'), max_length=255)
    message = models.TextField(_('Your Message'))
    published_at = models.DateTimeField(_('Publishing Date'), auto_now_add=True)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        db_table = 'contact_messages'
        ordering = ('-id',)
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def __str__(self):
        return self.subject
