from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null="True")
    slug = models.SlugField(unique=True, null=False)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="images", null="True", blank="True")

