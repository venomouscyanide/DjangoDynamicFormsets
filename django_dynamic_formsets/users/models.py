from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class TimeStampedModel(Model):
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Example2Model(TimeStampedModel):
    name = models.CharField(max_length=1024)
    email = models.EmailField()
    address = models.CharField(max_length=2048)
    phone_number = models.IntegerField()

    class Meta:
        verbose_name = "Example Two Form"
        verbose_name_plural = "Example Two Form"

    def __str__(self):
        return f"{self.name}:{self.email}"

