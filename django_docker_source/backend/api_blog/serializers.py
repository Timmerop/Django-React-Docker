from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
import logging

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.pw = validated_data.get('pw', instance.pw)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
