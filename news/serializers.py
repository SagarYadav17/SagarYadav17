from rest_framework import serializers

from news.models import Article


class ArticlesListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    source = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"

    def get_category(self, obj):
        return obj.category.name if obj.category else None

    def get_source(self, obj):
        return obj.source.name if obj.source else None
