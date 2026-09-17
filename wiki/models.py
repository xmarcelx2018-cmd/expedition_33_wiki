from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class WikiEntry(models.Model):
    title = models.CharField(max_length=60)
    category = models.CharField(
        max_length=20,
        choices=[
            ('character', 'Character'),
            ('weapon', 'Weapon'),
            ('location', 'Location'),
        ]
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='wiki_entries',
    )
    content = models.TextField(max_length=3000)
    image = CloudinaryField(
        'image',
        folder='wiki_images',
        blank=True,
        null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title