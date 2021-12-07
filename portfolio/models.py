
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(validators=[MinLengthValidator(10)])
    link = models.CharField(max_length=300)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return f"{self.title} ({self.date})"


# class Author(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# class Tag(models.Model):
#     caption = models.CharField(max_length=20)

#     def __str__(self):
#         return f"{self.caption}"
