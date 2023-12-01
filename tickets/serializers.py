from rest_framework import serializers

from .models import Tickets

class TicketsSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    status = serializers.ReadOnlyField()
    class Meta:
        model = Tickets
        fields = ['id', 'status', 'username', 'user', 'title', 'description', 'date']

        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True}
        }

class SingleTicketSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = Tickets
        fields = ['id', 'status', 'username', 'title', 'description', 'date']