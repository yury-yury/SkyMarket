from typing import List, Tuple

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class User(AbstractUser):
    """
    The User class is an inheritor of the AbstractUser class from the django.contrib.auth.models library.
    This is the data model contained in the user database table. Overrides and complements the description
    of the types and constraints of the fields of the base model.
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
        """
        The Meta class is used to change the behavior of model fields,
        such as verbose_name - a human-readable model name.
        """
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class Model and creates
        an output format for instances of this class.
        """
        return f"{self.email}, ({self.first_name} {self.last_name})"


    def image_(self):
        """
        The image_ function defines a class method. Accepts the instance itself as arguments. Adds the value
        of the image field to an instance of the User model, if this value is present in the request object.
        """
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="150"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_.short_description = 'Аватарка пользователя'
    image_.allow_tags = True

    def has_perm(self, perm, obj=None) -> bool:
        """
        The has_perm function overrides the method of the base class. Accepts the instance
        of the class itself, permissions and object as arguments. Returns a Boolean value, if the user has
        a permissions, then True, otherwise False.
        """
        return self.is_admin

    def has_module_perms(self, app_label) -> bool:
        """
        The has_module_perms function overrides the method of the base class. Accepts the instance
        of the class itself and app_label as arguments. Returns a Boolean value, if the user has
        a permissions, then True, otherwise False.
        """
        return self.is_admin

    @property
    def is_superuser(self) -> bool:
        """
        The is_superuser function overrides the property method of the base class. Accepts the instance
        of the class itself as argument. Returns a Boolean value, if the user is a superuser, then True,
        otherwise False.
        """
        return self.is_admin

    @property
    def is_staff(self) -> bool:
        """
        The is_staff function overrides the property method of the base class. Accepts the instance
        of the class itself as arguments. Returns a Boolean value, if the user is a staff, then True,
        otherwise False.
        """
        return self.is_admin

    @property
    def is_admin(self) -> bool:
        """
        The is_admin function overrides the property method of the base class. Accepts the instance
        of the class itself as arguments. Returns a Boolean value, if the user role is an admin, then True,
        otherwise False.
        """
        return self.role == 'admin'

    @property
    def is_user(self) -> bool:
        """
        The is_user function overrides the property method of the base class. Accepts the instance
        of the class itself as arguments. Returns a Boolean value, if the user role is a user, then True,
        otherwise False.
        """
        return self.role == 'user'


