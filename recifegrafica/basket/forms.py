# -*- coding: utf-8 -*-
from oscar.apps.basket.forms import BasketLineForm as CoreBasketLine

class BasketLineForm(CoreBasketLine):
    class Meta:
        fields = ['quantity','art_file', 'hire_art']
