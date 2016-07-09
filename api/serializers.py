from rest_framework import serializers

from api.models import User, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'users'
        model = User
        fields = ('id', 'full_name', 'email', 'password')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'users'
        model = User
        fields = ('id', 'full_name', 'email')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'posts'
        model = Post
        fields = ('id', 'title', 'text', 'user')


class PostGetSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()

    class Meta:
        db_table = 'posts'
        model = Post
        fields = ('id', 'title', 'text', 'user')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = 'comments'
        model = Comment
        fields = ('id', 'post', 'text', 'user')
