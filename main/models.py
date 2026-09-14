from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=150)
    title = models.CharField(max_length=200, help_text="Ex: Développeur Full Stack & Fondateur")
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile/')
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=100, blank=True)
    cv = models.FileField(upload_to='documents/', blank=True, null=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.full_name


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(blank=True, null=True, help_text="Laisser vide si en cours")
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_year']
        verbose_name = "Formation"
        verbose_name_plural = "Parcours académique"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=80, help_text="Niveau en % (0-100)")

    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Classe FontAwesome, ex: fa-solid fa-code")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=250, help_text="Séparées par des virgules, ex: Django, React, PostgreSQL")
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateField()

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        return [t.strip() for t in self.technologies.split(',')]


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Message"
        verbose_name_plural = "Messages de contact"

    def __str__(self):
        return f"{self.name} - {self.subject}"