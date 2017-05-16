from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import admin
from mzito.operation.models import Transformer, Location, Employee, Machinery
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save


class ApplicationManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ApplicationManager, self).filter(installed=False)


class Application(models.Model):
    transformer = models.ForeignKey(Transformer, related_name='transformer')
    distance = models.IntegerField('Distance from Transformer', default=0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='application')
    receipt_no = models.CharField('Receipt No:', max_length=30, null=True, blank=True)

    M_PESA = 'MPESA'
    KCB = 'KCB'
    LATER = 'NOT YET PAID'
    CO_OP = 'CO-OP'
    EQUITY = 'EQUITY'
    PAYMENT_METHODS = (
        (LATER, 'I will pay later'),
        (M_PESA, 'M-PESA paybill no. 34589'),
        (KCB, 'KCB Eldoret branch Account No. 12345670089'),
        (CO_OP, 'CO-OPERATIVE bank Account No 09872346875'),
        (EQUITY, 'EQUITY bank Account No 83294847829'),
        )
    payment_method = models.CharField('Your convenient payment method', null=True, blank=True,
                                      max_length=12, choices=PAYMENT_METHODS)
    amount = models.IntegerField('Amount Payed', default=0)
    installation = models.DateField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    message = models.TextField(null=True, blank=True)
    employee = models.ManyToManyField(Employee, related_name='employee')
    installed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("apply:application-detail", kwargs={"pk": self.id})

    class Meta:
        verbose_name = 'PowerApplication'
        verbose_name_plural = 'PowerApplications'

    def __str__(self):
        return '{0} at {1}'.format(self.user, self.transformer.location)


admin.site.register(Application)
