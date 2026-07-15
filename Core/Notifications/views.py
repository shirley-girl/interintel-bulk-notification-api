from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sender, Notification
from .serializers import SenderSerializer


# Create your views here.

class BulkNotificationView(APIView):
    def post(self, request):
        # Validation of incoming data
        serializer = SenderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        try:
            with transaction.atomic():
                validated_data = serializer.validated_data
                notifications_data = validated_data.pop('notifications', [])

                # create a sender
                sender = Sender.objects.create(**validated_data)

                # Notifications creation
                notification_objects = [
                    Notification(

                        sender=sender,
                        title=notification['title'],
                        message=notification['message'],
                        channel=notification['channel'],    
                    )
                    for notification in notifications_data
                ]
                Notification.objects.bulk_create(notification_objects)
                return Response(
                    {"status": "success",
                    "message": "Sender and notifications created successfully.",
                    "notifications_created" : len(notification_objects),
                    "sender_id" : sender.id,
                    },

                    status = status.HTTP_201_CREATED
            )
           
        except Exception as e:
            return Response({'error': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


