from oscar.apps.basket.abstract_models import AbstractLine as CoreLine, AbstractBasket as CoreBasket
from django.db import models

class Line(CoreLine):
    art_file = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)

class Basket(CoreBasket):
    def get_line(self, product_pk):
        for line in self.all_lines():
            if(product_pk == line.product.pk):
                string= line.product.pk
        return string



from oscar.apps.basket.models import *  # noqa
