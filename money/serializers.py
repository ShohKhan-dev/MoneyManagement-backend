# serializers.py
from rest_framework import serializers
from .models import Tag, Transaction

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TransactionSerializer(serializers.ModelSerializer):
    # tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    tag = TagSerializer(many=True, required=False)

    class Meta:
        model = Transaction
        fields = ['id', 'title', 'amount', 'datetime', 'transaction_type', 'description', 'tag']
    
    def create(self, validated_data):
        tags_data = validated_data.pop('tag', None)
        transaction = Transaction.objects.create(**validated_data)
        if tags_data:
            tags = []
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                tags.append(tag)
            transaction.tag.set(tags)
        return transaction

    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tag', None)
        instance = super().update(instance, validated_data)
        if tags_data:
            tags = []
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                tags.append(tag)
            instance.tag.set(tags)
        return instance

