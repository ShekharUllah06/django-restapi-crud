from rest_framework import serializers
from mobile.models import Phone


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"
