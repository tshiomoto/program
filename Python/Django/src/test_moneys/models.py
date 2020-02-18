from datetime import datetime
from django.db import models

# Create your models here.
class Item(models.Model):

    # define name of the table
    class Meta:
        db_table = "Item"
        verbose_name = "商品"
        verbose_name_plural = "商品"

    # entities
    item_name = models.CharField(verbose_name="品名", max_length=100, unique=True)
    price = models.IntegerField(verbose_name="値段", help_text="単位は円")

    def __str__(self):
        return self.item_name


class Person(models.Model):
    
    # define name of the table
    class Meta:
        db_table = "Person"
        verbose_name = "購入者リスト"
        verbose_name_plural = "購入者リスト"

    # entities
    person_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.person_name


class Buying(models.Model):

    # define name of the table
    class Meta:
        db_table = "Buying"
        verbose_name = "購入品リスト"
        verbose_name_plural = "購入品リスト"

    # entities
    buy_date = models.DateField(verbose_name="日付", default=datetime.now)
    buy_name = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="購入者")
    item_name = models.ForeignKey(Item, on_delete = models.PROTECT, verbose_name="商品")
    number = models.IntegerField(verbose_name="個数", default=1)

    def __str__(self):
        return str(self.buy_name) + "_" + str(self.item_name)