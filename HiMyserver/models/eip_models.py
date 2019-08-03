from django.db import models


class EIPDayTransferModels(models.Model):

    class Meta:
        verbose_name = "eip日流量计量查询"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return "eip日流量"


class BWSDayTransferModels(models.Model):

    class Meta:
        verbose_name = "bws日流量计量查询"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return "bws日流量"



