from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TicketsSerializer, SingleTicketSerializer, MessagesSerializer
from .models import Tickets, Messages

# Create your views here.

class TicketsListView(generics.ListCreateAPIView):
    model = Tickets
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.all().order_by("-date")
        
        user = self.request.user
        return Tickets.objects.filter(user=user).order_by("-date")
    
class SingleTicketView(generics.RetrieveUpdateAPIView):
    serializer_class = SingleTicketSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.all()
        
        user = self.request.user
        return Tickets.objects.filter(user=user)
    
    def delete(self, request, pk):
        ticket = Tickets.objects.filter(id=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TicketMessagesView(generics.ListCreateAPIView):
    serializer_class = MessagesSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pk = self.request.parser_context['kwargs']['id']
        if self.request.user.is_superuser:
            return Messages.objects.filter(ticket=pk).order_by("-date")

        user = self.request.user
        return Messages.objects.filter(ticket=pk).order_by("-date")
        

class UnresolvedTicketsView(generics.ListAPIView):
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.filter(status="unresolved").order_by("-date")
        
        return Tickets.objects.none()


class ResolvedTicketsView(generics.ListAPIView):
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.filter(status="resolved").order_by("-date")

        return Tickets.objects.none()


class FreezedTicketsView(generics.ListAPIView):
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.filter(status="freezed").order_by("-date")
        
        return Tickets.objects.none()
