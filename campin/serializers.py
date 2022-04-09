from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail', many=True, read_only=True)

    post_url = serializers.ModelSerializer.serializer_url_field(
        view_name='post_detail')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'date',
                  'owner', 'category', 'comments', 'post_url', 'photo')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail', read_only=True)

    post_id = serializers.PrimaryKeyRelatedField(
        source='post', queryset=Post.objects.all())

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'post', 'post_id', 'date', 'owner')
