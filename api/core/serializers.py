from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Data

class DataSerialiser(serializers.ModelSerializer):
    """Загруженные данные"""

    img = serializers.SerializerMethodField()
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Data
        fields = ('id', 'time', 'name',  'user', 'description', 'img',)

    def get_img(self, model):
        request = self.context.get('request')
        img = model.img.url
        return request.build_absolute_uri(img)

