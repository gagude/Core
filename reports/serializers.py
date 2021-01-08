from rest_framework import serializers
from .models import Article

#Create Serializers Here
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['article_body']