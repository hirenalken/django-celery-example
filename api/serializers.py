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
        fields = ('id', 'post', 'c_text', 'user')


class PostDetailSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    id = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.CharField()

    user = UserInfoSerializer()
    comment = serializers.SerializerMethodField()

    def get_comment(self, instance):
        try:
            if instance.comment_set.all().exists():
                return CommentSerializer(instance.comment_set.all()[0]).data
            else:
                return None
        except Comment.DoesNotExist:
            return None

