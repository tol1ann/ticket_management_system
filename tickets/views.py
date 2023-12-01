from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TicketsSerializer, SingleTicketSerializer
from .models import Tickets

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
    

class UnresolvedTicketsView(generics.ListAPIView):
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.filter(status="unresolved").order_by("-date")
        

class ResolvedTicketsView(generics.ListAPIView):
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.filter(status="resolved").order_by("-date")
        

class FreezedTicketsView(generics.ListAPIView):
    serializer_class = TicketsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tickets.objects.filter(status="freezed").order_by("-date")