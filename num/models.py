from django.db import models


class Prime(models.Model):
    name = models.CharField(max_length=50)
    fnum = models.IntegerField()
    lnum = models.BigIntegerField()

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "prim_num"
