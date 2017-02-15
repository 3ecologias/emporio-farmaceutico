from oscar.apps.promotions.models import AbstractProductList as CoreAbstractProductList
from django.utils.translation import ugettext_lazy as _
from django.db import models

class AutomaticProductList(CoreAbstractProductList):
    BESTSELLING_PER_CATEGORY = ('Bestselling category')




from oscar.apps.promotions.models import *  # noqa
