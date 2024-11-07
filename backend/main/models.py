from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact de {self.full_name}"
    


class Quotation(models.Model):
    CONTRACT_CHOICES = [
        ('residential', 'Résidentiel'),
        ('commercial', 'Commercial'),
        ('industrial', 'Industriel'),
    ]

    full_name = models.CharField(max_length=255, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    address = models.CharField(max_length=255, verbose_name="Adresse")
    contract_type = models.CharField(max_length=50, choices=CONTRACT_CHOICES, verbose_name="Type de contrat souhaité")
    estimated_consumption = models.PositiveIntegerField(verbose_name="Consommation estimée (kWh)")
    message = models.TextField(verbose_name="Message")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Devis de {self.full_name} pour un contrat {self.contract_type}"
    


class Blog(models.Model):


    title = models.CharField(max_length=255, verbose_name="Titre")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name="Auteur")
    content = models.TextField(verbose_name="Contenu")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de mise à jour")
    published_at = models.DateTimeField(default=timezone.now, verbose_name="Date de publication")
    image = models.ImageField(upload_to='', blank=True, null=True, verbose_name="Image")

    class Meta:
        ordering = ['-published_at']
        verbose_name = "Post de blog"
        verbose_name_plural = "Posts de blog"

    def __str__(self):
        return self.title        
    
    
    
