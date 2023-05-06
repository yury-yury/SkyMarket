from typing import List
from django.db import models

from users.models import User


class Ad(models.Model):
    """
    The Ad class is an inheritor of the Model class from the django.db.models module. It is a data model contained
    in the ads database table. Contains a description of the types and constraints of the model fields.
    """
    title = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True, default=None)

    class Meta:
        """
        The Meta class is used to change the behavior of model fields, such as verbose_name - the human-readable
        name of the model. And contains rules for sorting ads during output.
        """
        verbose_name: str = 'Объявление'
        verbose_name_plural: str = 'Объявления'
        ordering: List[str] = ['-created_at', ]

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class Model and creates
        an output format for instances of this class.
        """
        return self.title


class Comment(models.Model):
    """
    The Comment class is an inheritor of the Model class from the models library. It is a data model contained
    in the ads database table. Contains a description of the types and constraints of the model fields.
    """
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        The Meta class is used to change the behavior of model fields, such as verbose_name - the human-readable
        name of the model. And contains rules for sorting comments during output.
        """
        verbose_name: str = 'Комментарий'
        verbose_name_plural: str = 'Комментарии'
        ordering: List[str] = ['-created_at']

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class Model and creates
        an output format for instances of this class.
        """
        return self.text
