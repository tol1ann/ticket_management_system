from rest_framework import serializers

from .models import Tickets, Messages

class TicketsSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    status = serializers.ReadOnlyField()

    class Meta:
        model = Tickets
        fields = ['id', 'status', 'username', 'user', 'title', 'description', 'date']


class CreateTicketSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    status = serializers.ReadOnlyField()
   
    class Meta:
        model = Tickets
        fields = ['id', 'status', 'username', 'title', 'description', 'date']

        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        ticket = Tickets.objects.create(**validated_data)

        return ticket

class SingleTicketSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    title = serializers.ReadOnlyField()
    description = serializers.ReadOnlyField()

    class Meta:
        model = Tickets
        fields = ['id', 'status', 'username', 'title', 'description', 'date']


class MessagesSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    ticket_id = Messages.ticket

    class Meta:
        model = Messages
        fields = ['username', 'date', 'message', 'ticket_id'] 

    def create(self, validated_data):
        message = Messages.objects.create(**validated_data)
        
        return message