from django.db import models



from django.contrib.auth.models import User
from django_resized import ResizedImageField

# python manage.py dumpdata blogs.Tag --output blogs/fixtures/Tag.test.json
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




def uploadedform(object,filename):
    try:
        import pathlib
        file_extension = pathlib.Path(filename).suffix

        return f'blogs/{object.title}{file_extension}'

    except Exception as e:
        print(f"error uploading gallery,{e}")

# python manage.py dumpdata auth.User --output main/fixtures/users.static.json
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="post_author")
    image = ResizedImageField(upload_to=uploadedform)
    tags = models.ManyToManyField(Tag)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
