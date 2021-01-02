from django.db import models
from django.conf import settings

# custom token model dependencies
from django.utils.translation import gettext as _

# Postgresql specific field
from django.contrib.postgres.fields import ArrayField

# 3rd party/standard
import uuid
import binascii
import os


# Custom Token class (has all fields of Token minus User)
# the user column is replaced with Node for authentication
# of EOH nodes utilizing token auth
class NodeToken(models.Model):
    """
    The default authorization token model.

    sourced with print(inspect.getsource(Token)), simply deleted removed user entry
    """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    '''user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )'''
    ## CUSTOM FIELD 'node' replaces user default above
    node = models.OneToOneField(
        settings.AUTH_NODE_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("Node")
    )

    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
        verbose_name = _("NodeToken")
        verbose_name_plural = _("NodeTokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


# EOH Node Model
# only registers new nodes into database if the owner has initialized it into a cluster
class Node(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default = uuid.uuid4, 
        editable = False,
    )
    ip_address = models.GenericIPAddressField(unique=True)
    name = models.CharField(max_length=100)
    initialized = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    cluster = models.ForeignKey('core.Cluster', related_name='nodes', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)




### EOH node data logs ###

# EOH Node Performance (cpu, gpu, memory, temps) data storage table
class Performance(models.Model):

    def general_default():
        return ['cpu_freq', 'cpu_usage', 'mem_usage', 'mem_avail', 'mem_perc']

    def cpu_default():
        return ['cpu_freq', 'cpu_usage', 'mem_usage', 'mem_avail', 'mem_perc']

    def gpu_default():
        return ['cpu_freq', 'cpu_usage', 'mem_usage', 'mem_avail', 'mem_perc']

    node = models.ForeignKey(
        'Node',
        on_delete=models.CASCADE,
        to_field="id"
    )
    general_columns = ArrayField(models.CharField(max_length=30), default=general_default)
    general_data = models.FileField(upload_to='performance/%Y/%m/general')

    cpu_columns = ArrayField(models.CharField(max_length=30), default=gpu_default)
    cpu_data = models.FileField(upload_to='performance/%Y/%m/cpu')

    gpu_columns = ArrayField(models.CharField(max_length=30), default=cpu_default)
    gpu_data = models.FileField(upload_to='performance/%Y/%m/gpu')

    data_start = models.DateTimeField(blank=True, null=True)
    data_end = models.DateTimeField(blank=True, null=True)
    rows = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.node)

    class Meta:
        verbose_name = 'Performance'
        verbose_name_plural = 'Performance'







'''

# EOH Node Performance (cpu, memory, temps) data storage table
class Performance(models.Model):

    def columns_default():
        return ['cpu_freq', 'cpu_usage', 'mem_usage', 'mem_avail', 'mem_perc']

    node = models.ForeignKey(
        'Node',
        on_delete=models.CASCADE
    )
    data_columns = ArrayField(models.CharField(max_length=30, blank=True), default=columns_default)
    data_start = models.DateTimeField(blank=True, null=True)
    data_end = models.DateTimeField(blank=True, null=True)
    rows = models.IntegerField(default=0)
    initialized = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.node

    class Meta:
        verbose_name = 'Performance'
        verbose_name_plural = 'Performance'


# EOH Node Performance (cpu, memory, temps) data storage table
class Performance(models.Model):

    def columns_default():
        return ['cpu_freq', 'cpu_usage', 'mem_usage', 'mem_avail', 'mem_perc']

    node = models.ForeignKey(
        'Node',
        on_delete=models.CASCADE
    )
    data_columns = ArrayField(models.CharField(max_length=30, blank=True), default=columns_default)
    data_start = models.DateTimeField(blank=True, null=True)
    data_end = models.DateTimeField(blank=True, null=True)
    rows = models.IntegerField(default=0)
    initialized = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.node

    class Meta:
        verbose_name = 'Performance'
        verbose_name_plural = 'Performance'

'''