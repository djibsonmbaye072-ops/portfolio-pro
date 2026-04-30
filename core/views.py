from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os
from datetime import date

from .models import Project, Experience, Skill, Certification


# =========================
# HOME PAGE
# =========================
def home(request):
    projects = Project.objects.filter(is_active=True).order_by('-created_at')

    return render(request, 'core/home.html', {
        'projects': projects
    })


# =========================
# ABOUT PAGE
# =========================
def about(request):
    return render(request, 'core/about.html')


# =========================
# PROJECTS PAGE (REALISATIONS)
# =========================
def projects(request):
    projects = Project.objects.filter(is_active=True).order_by('-created_at')

    return render(request, 'core/projects.html', {
        'projects': projects
    })


# =========================
# PROJECT DETAIL PAGE 🔥
# =========================
def project_detail(request, id):
    project = get_object_or_404(
        Project,
        id=id,
        is_active=True
    )

    return render(request, 'core/project_detail.html', {
        'project': project
    })


# =========================
# EXPERIENCE PAGE (ULTRA INTELLIGENT)
# =========================
def experience(request):

    experiences = Experience.objects.filter(
        is_active=True
    ).order_by(
        'order',
        '-start_date',
        '-created_at'
    )

    # 🔥 préparation des skills
    for exp in experiences:
        if exp.skills:
            exp.skills_list = [
                skill.strip() for skill in exp.skills.split(',')
            ]
        else:
            exp.skills_list = []

    # 🔥 compteur
    total_experiences = experiences.count()

    # 🔥 calcul années expérience
    total_days = 0

    for exp in experiences:
        if exp.start_date:
            end_date = exp.end_date if exp.end_date else date.today()
            total_days += (end_date - exp.start_date).days

    total_years = round(total_days / 365) if total_days > 0 else 0

    return render(request, 'core/experience.html', {
        'experiences': experiences,
        'total_experiences': total_experiences,
        'total_years': total_years
    })


# =========================
# SKILLS PAGE (DYNAMIQUE 🔥)
# =========================
def skills(request):

    skills = Skill.objects.all()
    certifications = Certification.objects.all()

    # 🔥 regroupement par catégorie
    categories = {
        'dev': [],
        'bio': [],
        'it': [],
        'soft': []
    }

    for skill in skills:
        if skill.category in categories:
            categories[skill.category].append(skill)

    return render(request, 'core/skills.html', {
        'categories': categories,
        'certifications': certifications
    })


# =========================
# DOWNLOAD CV PDF 🔥 (SAFE VERSION)
# =========================
def download_cv(request):

    file_path = os.path.join(settings.MEDIA_ROOT, 'cv.pdf')

    # 🔥 sécurité : éviter crash si fichier absent
    if os.path.exists(file_path):
        return FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
            filename='DJIBRIL_MBAYE_CV.pdf'
        )
    else:
        return HttpResponse("⚠️ CV introuvable. Ajoute le fichier dans /media/cv.pdf")