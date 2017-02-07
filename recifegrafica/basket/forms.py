# -*- coding: utf-8 -*-
from oscar.apps.basket.forms import BasketLineForm as CoreBasketLine
from django.forms import forms

class BasketLineForm(CoreBasketLine):
    class Meta:
        fields = ['quantity','art_file', 'hire_art']
        labels = { 'art_file': 'Selecione um arquivo', 'hire_art': 'enviar'}

    def clean(self):
        clean_data = self.cleaned_data
        is_hire_art = clean_data.get("hire_art")
        have_art_file = clean_data.get("art_file")
        if not is_hire_art and not have_art_file:
            raise forms.ValidationError(
                "É necessário enviar o arquivo da arte, ou contratar o serviço de arte"
            )
        elif is_hire_art and have_art_file:
            raise forms.ValidationError(
                "Selecione apenas uma opção"
            )
