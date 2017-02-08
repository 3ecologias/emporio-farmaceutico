# -*- coding: utf-8 -*-

from oscar.apps.customer.forms import EmailUserCreationForm as CoreUserCreationForm
from oscar.core.compat import (get_user_model)
from django import forms
from localflavor.br.forms import BRCNPJField, BRCPFField
from django.utils.translation import ugettext_lazy as _
User = get_user_model()

class EmailUserCreationForm(CoreUserCreationForm):

    PERSONA_CHOICES = (('fs','Física'),('jr', 'Jurídica'))

    persona = forms.CharField(label=_('Personalidade'), required=True,widget=forms.Select(choices=PERSONA_CHOICES))
    cnpj = BRCNPJField(label=_('CNPJ'), required=False)
    cpf = BRCPFField(label=_('CPF'), required=False)
    class Meta:
        model = User
        fields = ('email','persona', 'cnpj', 'cpf')
