# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Cliente_{0}/{1}'.format(instance.user, filename)


class Document(models.Model):
    user = models.ForeignKey(User, null=True)
    order_number = models.CharField("Número da ordem", max_length=255, blank=True, null=True)
    document = models.FileField("Arquivo da arte", upload_to=user_directory_path)
    product_description = models.CharField("Descrição do produto", max_length=500, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    

class UploadForm(ModelForm):
	class Meta:
		model = Document
		fields = ('order_number', 'document', 'product_description',)
