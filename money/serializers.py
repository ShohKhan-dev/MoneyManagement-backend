# serializers.py
from rest_framework import serializers
from .models import Tag, Transaction
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        read_only_fields = ('id',)



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TransactionSerializer(serializers.ModelSerializer):
    # tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    tag = TagSerializer(many=True, required=False)
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Transaction
        fields = ['id', 'title', 'amount', 'datetime', 'author', 'transaction_type', 'description', 'tag']
    
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

