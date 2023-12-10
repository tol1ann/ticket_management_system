from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, NotFound

from .serializers import *
from .models import Tickets, Messages

# Create your views here.

class TicketsListView(generics.ListAPIView):
    model = Tickets
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.all().order_by("-date")
        
        user = self.request.user
        return Tickets.objects.filter(user=user).order_by("-date")
    

class CreateTicketView(generics.CreateAPIView):
    serializer_class = CreateTicketSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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
       
        raise NotFound("404 Not Found")
    

class TicketMessagesView(generics.ListCreateAPIView):
    queryset = Messages.objects.all().order_by("-date")
    serializer_class = MessagesSerializer
    permission_classes = [IsAuthenticated]


    def get_ticket(self):
        pk = self.request.parser_context['kwargs']['id']
        ticket = Tickets.objects.get(id=pk)

        return ticket

    def perform_create(self, serializer):
            serializer.save(user=self.request.user, ticket=self.get_ticket())

    def get_queryset(self):
        pk = self.request.parser_context['kwargs']['id']
        return Messages.objects.filter(ticket_id=pk).order_by("-date")


class UnresolvedTicketsView(generics.ListAPIView):
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.filter(status="unresolved").order_by("-date")
        
        raise PermissionDenied("403 Forbidden")


class ResolvedTicketsView(generics.ListAPIView):
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.filter(status="resolved").order_by("-date")

        raise PermissionDenied("403 Forbidden")


class FreezedTicketsView(generics.ListAPIView):
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.filter(status="freezed").order_by("-date")
        
        raise PermissionDenied("403 Forbidden")
