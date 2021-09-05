import datetime
import random
from itertools import islice

from django.db import models


class Handbook(models.Model):
    '''Model for handbooks'''

    title = models.CharField(max_length=255, default='', blank=True)
    mini_title = models.CharField(max_length=255, default='', blank=True)
    description = models.CharField(max_length=255, default='', blank=True)
    start_date = models.DateField(blank=True, null=True)
    version = models.ForeignKey('Version', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Version(models.Model):
    '''Model for versions of handbook'''

    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Element(models.Model):
    '''Model for element of handbook'''

    handbook = models.ForeignKey(Handbook, on_delete=models.CASCADE, related_name='element')
    code = models.CharField(max_length=255, default='code')
    value = models.CharField(max_length=255, default='value')

    def __str__(self):
        return self.value


def insert_post_bulk_elem(batch_size):
    objs = (Element(code=f'code {i}', value=f'value {i}', handbook_id=random.randint(1, 99)) for i in range(batch_size))
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        Element.objects.bulk_create(batch, batch_size)


def insert_post_bulk_handbook(batch_size):
    objs = (Handbook(title=f'title {i}', mini_title=f'mini_title {i}', description=f'description {i}',
                     start_date=datetime.datetime.now(), version_id=random.randint(1, batch_size)) for i in
            range(batch_size))
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        Handbook.objects.bulk_create(batch, batch_size)


def insert_post_bulk_version(batch_size):
    objs = (Version(title=f'title {i}') for i in range(batch_size))
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        Version.objects.bulk_create(batch, batch_size)
