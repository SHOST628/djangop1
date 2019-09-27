from django.db import models


# Create your models here.
class BookInfo(models.Model):
    """Book model class"""
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    # bprice = models.DecimalField(max_digits=10, decimal_places=2)
    # reading quantity
    bread = models.IntegerField(default=0)
    # comment quantity
    bcomment = models.IntegerField(default=0)
    # delete flag (soft delete)
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    """Hero model class"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200, null=True, blank=True)
    # relation property
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)


class AreaInfo(models.Model):
    """Area model class"""
    # area name
    atitle = models.CharField(max_length=20)
    # relations property, represent for parent area
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
