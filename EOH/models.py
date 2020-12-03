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
    ip_address = models.GenericIPAddressField(unique=True)
    name = models.CharField(max_length=100)
    initialized = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    cluster = models.ForeignKey('core.Cluster', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)




### Systems data storage ###
#
# Each model revolves around a csv file containing the 
# time series data with in the scope of data_start, data_end
# and in the columns of data_columns. The first column is the
# timestamp and a new entry for the same node will be made 
# at a time interval to prevent an individual file from getting
# too large. (currently shooting for a 30 day window for each
# new file)

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