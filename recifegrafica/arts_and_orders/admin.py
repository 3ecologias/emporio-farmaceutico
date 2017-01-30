from django.contrib import admin
from .models import *
from django.utils.encoding import smart_unicode as _

admin.site.register(Document)
