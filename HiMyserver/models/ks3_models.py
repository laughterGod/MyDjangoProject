from django.db import models


class KS3Models(models.Model):

    class Meta:
        verbose_name = "ks3日存储量计量查询"  # 表名改成中文名
        verbose_name_plural = verbose_name

    def __str__(self):
        return "ks3存储量"

