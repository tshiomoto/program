from datetime import datetime
from django.db import models

# Create your models here.
class Item(models.Model):

    # define name of the table
    class Meta:
        db_table = "Item"

    # entities
    item_name = models.CharField(max_length=100, unique=True)


class Buying(models.Model):

    # define name of the table
    class Meta:
        db_table = "Buying"

    # entities
    buy_date = models.DateField(verbose_name="日付", default=datetime.now)
    item = models.ForeignKey(Item, on_delete = models.PROTECT, verbose_name="商品")
    price = models.IntegerField(verbose_name="値段", help_text="単位は円")
