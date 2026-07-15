from rest_framework import serializers

from .models import Sender, Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification

        fields = (
            'title',
            'message',
            'channel',
        )


class SenderSerializer(serializers.ModelSerializer):

    notifications = NotificationSerializer(many=True)

    class Meta:
        model = Sender

        fields = (
            'name',
            'email',
            'notifications',
        )

    def validate_notifications(self, value):
        if not value:
            raise serializers.ValidationError(
                "At least one notification is required."
                )
        return value