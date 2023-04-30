from typing import List, Tuple

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class User(AbstractUser):
    """

    """
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    ROLE: List[Tuple[str, str]] = [('user', 'Пользователь'),
                                   ('admin', 'Администратор')]

    role = models.CharField(max_length=5, choices=ROLE, default='user')
    email = models.EmailField(_("email address"), unique=True)
    phone = PhoneNumberField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def image_(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="150"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_.short_description = 'Аватарка пользователя'
    image_.allow_tags = True

    def __str__(self):
        """

        """
        return f"{self.email}, ({self.first_name} {self.last_name})"

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_user(self):
        return self.role == 'user'


