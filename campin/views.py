from rest_framework import generics, permissions
from .models import Campground, Review, Post, Comment, Mycampin
from .serializers import CampgroundSerializer, ReviewSerializer, PostSerializer, CommentSerializer, MycampinSerializer
from .permissions import IsOwnerOrReadOnly


class CampgroundList(generics.ListCreateAPIView):
    queryset = Campground.objects.all()
    serializer_class = CampgroundSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CampgroundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campground.objects.all()
    serializer_class = CampgroundSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]


class MycampinList(generics.ListCreateAPIView):
    queryset = Mycampin.objects.all()
    serializer_class = MycampinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MycampinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mycampin.objects.all()
    serializer_class = MycampinSerializer
    permission_classes = [IsOwnerOrReadOnly]
