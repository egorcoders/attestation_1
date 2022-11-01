from rest_framework import serializers

from .models import EmergencyService, Applicant, Request


class EmergencyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyService
        fields = '__all__'


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    applicant = serializers.SlugRelatedField(read_only=True, slug_field='patronymic')
    emergency_service = serializers.SlugRelatedField(read_only=True, many=True, slug_field='service_name')

    class Meta:
        model = Request
        fields = '__all__'
