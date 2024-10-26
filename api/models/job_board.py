from django.db import models

from api.models.user import CustomUser


class JobSeeker(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    resume = models.URLField(max_length=2000, null=True, blank=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        name_parts = [part for part in (self.first_name, self.last_name) if part]
        return " ".join(name_parts) if name_parts else self.user.email


class Employer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo_url = models.URLField(max_length=2000, null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.company_name or self.user.email


class Job(models.Model):
    EMPLOYMENT_TYPE_CHOICES = [
        ("FT", "Full-time"),
        ("PT", "Part-time"),
        ("CT", "Contract"),
        ("IN", "Internship"),
    ]

    title = models.CharField(max_length=100)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=2, choices=EMPLOYMENT_TYPE_CHOICES)
    posted_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.employer.company_name}"


class Application(models.Model):
    STATUS_CHOICES = [
        ("P", "Pending"),
        ("R", "Reviewed"),
        ("I", "Interviewed"),
        ("A", "Accepted"),
        ("D", "Declined"),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="P")
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.applicant.user.username}'s application for {self.job.title}"
