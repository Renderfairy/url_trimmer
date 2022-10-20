from django.contrib.auth import get_user_model
from django.db import models


class SaveURL(models.Model):
    """
    Stores a single url entry, related to :model:users.CustomUser
    """
    url = models.URLField(max_length=300)
    alias = models.URLField(max_length=100, default=0, unique=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='urls')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.url)
