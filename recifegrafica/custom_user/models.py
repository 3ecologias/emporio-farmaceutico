from __future__ import unicode_literals

from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser
from localflavor.br.forms import BRCNPJField, BRCPFField

class User(AbstractUser):
    cpf = models.CharField("CPF", max_length=14, null=True, blank=True)
    cnpj = models.CharField("CNPJ", max_length=18, null=True, blank=True)
