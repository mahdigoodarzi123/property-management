from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    LOCATION_CHOICES = [
        ('ساختمان شماره یک', 'ساختمان شماره یک'),
        ('ساختمان شماره دو', 'ساختمان شماره دو'),
    ]

    FLOOR_CHOICES = [
        ('لابی', 'لابی'),
        ('طبقه یک', 'طبقه یک'),
        ('طبقه دو', 'طبقه دو'),
        ('طبقه سه', 'طبقه سه'),
        ('طبقه چهار', 'طبقه چهار'),
        ('طبقه پنج', 'طبقه پنج'),
        ('طبقه شش', 'طبقه شش'),
    ]

    code = models.CharField(max_length=100, verbose_name="کد اموال")
    group = models.CharField(max_length=100, verbose_name="گروه")
    description = models.TextField(verbose_name="شرح")
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, verbose_name="محل")
    floor = models.CharField(max_length=20, choices=FLOOR_CHOICES, verbose_name="طبقه")
    status = models.CharField(max_length=100, verbose_name="وضعیت")
    census_1403 = models.CharField(max_length=100, blank=True, null=True, verbose_name="سرشماری 1403")
    room = models.CharField(max_length=100, blank=True, null=True, verbose_name="اتاق")
    user = models.CharField(max_length=100, verbose_name="استفاده کننده")
    vendor = models.CharField(max_length=100, blank=True, null=True, verbose_name="فروشنده")
    notes = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)



    def __str__(self):
        return self.code