from django.db import models


# =========================
# PROJECT MODEL (PORTFOLIO PRO)
# =========================
class Project(models.Model):

    CATEGORY_CHOICES = [
        ('web', 'Web'),
        ('bio', 'Biomédical'),
        ('other', 'Autres'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()

    # image principale (hero)
    image = models.ImageField(upload_to='projects/')

    # lien externe (optionnel)
    link = models.URLField(blank=True, null=True)

    # catégorie pour filtre
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='web'
    )

    # organisation
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# =========================
# PROJECT GALLERY (ULTRA PRO)
# =========================
class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return f"Image - {self.project.title}"


# =========================
# EXPERIENCE MODEL (TIMELINE PRO)
# =========================
class Experience(models.Model):

    SIDE_CHOICES = [
        ('left', 'Gauche'),
        ('right', 'Droite'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, null=True)

    # dates réelles
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # affichage automatique
    period = models.CharField(max_length=100, blank=True)

    description = models.TextField()

    # image optionnelle
    image = models.ImageField(upload_to='experiences/', blank=True, null=True)

    # position timeline
    side = models.CharField(max_length=10, choices=SIDE_CHOICES, default='left')

    # badges dynamiques (string séparée par virgule)
    skills = models.CharField(
        max_length=300,
        blank=True,
        help_text="Ex: Django, Python, API, Maintenance"
    )

    # organisation
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    # =========================
    # AUTO PERIOD GENERATION
    # =========================
    def save(self, *args, **kwargs):

        if self.start_date:
            if self.end_date:
                self.period = f"{self.start_date.year} - {self.end_date.year}"
            else:
                self.period = f"{self.start_date.year} - Présent"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.period})"

    class Meta:
        ordering = ['order', '-start_date', '-created_at']

# =========================
# SKILL MODEL (DYNAMIQUE)
# =========================
class Skill(models.Model):

    CATEGORY_CHOICES = [
        ('dev', 'Développement'),
        ('bio', 'Biomédical'),
        ('it', 'IT & Réseaux'),
        ('soft', 'Soft Skills'),
    ]

    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="Pourcentage (0-100)")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.level}%)"


# =========================
# CERTIFICATION MODEL
# =========================
class Certification(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.organization}"