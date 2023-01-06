from django.db import models

class Article(models.Model):
    nom = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
