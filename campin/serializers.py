from rest_framework import serializers
from .models import Campground, Review, Post, Comment, Mycampin


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    campground = serializers.HyperlinkedRelatedField(
        view_name='campground_detail', read_only=True)

    campground_id = serializers.PrimaryKeyRelatedField(
        source='campground', queryset=Campground.objects.all())

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'body', 'campground',
                  'campground_id', 'date', 'owner', 'rating')


class CampgroundSerializer(serializers.HyperlinkedModelSerializer):
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    campground_url = serializers.ModelSerializer.serializer_url_field(
        view_name='campground_detail')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Campground
        fields = ('id', 'name', 'body', 'date',
                  'owner', 'reviews', 'location', 'campground_url', 'photo')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail', read_only=True)

    post_id = serializers.PrimaryKeyRelatedField(
        source='post', queryset=Post.objects.all())

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'post', 'post_id', 'date', 'owner')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    post_url = serializers.ModelSerializer.serializer_url_field(
        view_name='post_detail')

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'date',
                  'owner', 'category', 'comments', 'post_url', 'photo')


class MycampinSerializer(serializers.Serializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Mycampin
        fields = ('id', 'body', 'date', 'owner')
