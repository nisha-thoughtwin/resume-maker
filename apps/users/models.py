from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
class User(AbstractUser):
    account_approved = models.BooleanField(default=False)
    is_teamleader = models.BooleanField(default=False)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children",
        help_text="don't forget to check is_teamleader if parent is set",
    )

    def clean(self):
        super().clean()
        try:
            user=User.objects.get(username=self.username)
        except user.DoesNotExist:
            self.password = make_password(self.password)
        return self.password