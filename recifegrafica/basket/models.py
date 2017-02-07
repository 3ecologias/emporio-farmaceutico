# -*- coding: utf-8 -*-
from oscar.apps.basket.abstract_models import AbstractLine as CoreLine, AbstractBasket as CoreBasket
from django.db import models
import os

class Line(CoreLine):
    art_file = models.FileField("Arquivo de arte", upload_to="Temp/", null=True, blank=True)
    hire_art = models.BooleanField("Contratou serviço de arte?", default=False)

    def filename(self):
        return os.path.basename(self.art_file.name)


from oscar.apps.basket.models import *  # noqa
