from rest_framework import serializers

from . import models


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.URL
        fields = ['url', 'alias']
