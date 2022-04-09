from django.db import models

category_select = (
    ('Talk Talk!', 'Talk Talk!'),
    ('Reviews', 'Reviews'),
    ('Q & A', 'Q & A'),
    ('Tips', 'Tips'),
    ('Market', 'Market'),
)


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'users.User', related_name='posts', on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='images/', default='images/default.webp', blank=True)
    category = models.CharField(
        max_length=20, choices=category_select, default='Talk Talk!')

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.CharField(max_length=500)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'users.User', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.body
