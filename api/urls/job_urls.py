from django.urls import path

from api.views.job_views import JobDetailBySlugView, JobDetailView, JobListCreateView

urlpatterns = [
    path("jobs/", JobListCreateView.as_view(), name="job-list-create"),
    path("jobs/<uuid:pk>/", JobDetailView.as_view(), name="job-detail"),
    path(
        "jobs/slug/<str:slug>/",
        JobDetailBySlugView.as_view(),
        name="job-detail-by-slug",
    ),
]
