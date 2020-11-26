from django.db import models
# Postgresql specific field
from django.contrib.postgres.fields import ArrayField

# 3rd party
import uuid


# EOH Node Model
# only registers new nodes into database if the owner has initialized it into a cluster
class Node(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default = uuid.uuid4, 
        editable = False,
    )
    #ip_address = models.GenericIPAddressField(unique=True)
    name = models.CharField(max_length=100)
    initialized = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    #cluster = models.ForeignKey('core.Cluster', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uuid)



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