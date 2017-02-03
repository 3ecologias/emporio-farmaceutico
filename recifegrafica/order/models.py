from oscar.apps.order.abstract_models import AbstractLine
from django.db import models
from django.conf import settings
import os
from django.core.files.base import ContentFile


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Ordem de numero {0}/{1}'.format(instance.order.number, filename)

class Line(AbstractLine):
    art_file = models.FileField("Arquivo da arte", null=True, upload_to=user_directory_path, blank=True)

    def changeFileDirectory(self, name):
        line = Line.objects.get(id=self.id)
        file_ = ContentFile(line.art_file.read())
        file_.name = "{}".format(name)
        line.art_file = file_
        line.save()

    def filename(self):
        return os.path.basename(self.art_file.name )

from oscar.apps.order.models import *
