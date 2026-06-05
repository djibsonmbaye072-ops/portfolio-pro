from django.contrib import admin
from .models import Project, Experience, Skill, Certification


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_at',
        'is_active'
    )

    list_filter = (
        'is_active',
        'created_at'
    )

    search_fields = (
        'title',
        'description'
    )

    fieldsets = (
        (
            "Informations",
            {
                "fields": (
                    "title",
                    "description",
                    "image",
                    "link",
                    "is_active",
                )
            },
        ),

        (
            "Étude de cas",
            {
                "fields": (
                    "problem",
                    "solution",
                    "results",
                    "technologies",
                )
            },
        ),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'period',
        'is_active'
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'title',
        'company',
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'level',
        'category'
    )

    list_filter = (
        'category',
    )

    search_fields = (
        'name',
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'organization',
        'year'
    )

    list_filter = (
        'year',
    )

    search_fields = (
        'title',
        'organization',
    )