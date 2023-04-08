# serializers.py
from rest_framework import serializers
from .models import Tag, Category, Transaction

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tag = TagSerializer(many=True, required=False)

    class Meta:
        model = Transaction
        fields = ['id', 'title', 'amount', 'datetime', 'transaction_type', 'description', 'category', 'tag']

