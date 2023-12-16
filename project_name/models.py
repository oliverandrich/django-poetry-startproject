from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(DirtyFieldsMixin, models.Model):
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return super().__str__()
