from django.contrib.auth import get_user_model
from django.db import models
from django.utils.crypto import get_random_string


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class URL(models.Model):
    """
    Stores a single url entry, related to :model:users.CustomUser
    """
    url = models.URLField(max_length=300)
    alias = models.URLField(max_length=100, default=0, unique=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='urls')
    created_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('Category', related_name='urls')

    class Meta:
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = get_random_string(length=10)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
