from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime, naturalday

from datetime import date
from news.models import Article


class ArticlesListSerializer(serializers.ModelSerializer):
    title =serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    source = serializers.SerializerMethodField()
    publishedAt = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"
    
    def get_title(self, obj):
        return obj.title.split(' - ')[0]

    def get_category(self, obj):
        return obj.category.name if obj.category else None

    def get_source(self, obj):
        return obj.source.name if obj.source else None

    def get_publishedAt(self, obj):
        if obj.publishedAt.date() == date.today():
            return naturaltime(obj.publishedAt)
        else:
            return naturalday(obj.publishedAt)
    
    def get_country(self, obj):
        return obj.country.name if obj.country else None
