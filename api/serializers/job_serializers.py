from rest_framework import serializers

from api.models import Employer, Job


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ["company_name", "logo_url"]


class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="employer.company_name", read_only=True)
    logo_url = serializers.URLField(source="employer.logo_url", read_only=True)

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "requirements",
            "salary",
            "location",
            "company_name",
            "logo_url",
            "posted_date",
            "employment_type",
        ]
        read_only_fields = ["posted_date", "slug", "company_name", "logo_url"]

    def create(self, validated_data):
        validated_data["employer"] = self.context["request"].user.employer
        job = Job.objects.create(**validated_data)
        return job
