from django.contrib.auth import get_user_model
from django.db import models


class SaveURL(models.Model):
    url = models.URLField(max_length=300)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='urls')

    def __str__(self):
        return str(self.url)
