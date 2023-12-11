from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

from .models import Tickets, Messages


class CreateTicketViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_ticket_view(self):
        data = {
            'title': 'test_title',
            'description': 'test_description'
        }
        response = self.client.post(reverse('create-ticket'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tickets.objects.count(), 1)
        self.assertEqual(Tickets.objects.first().user, self.user)


class SingleTicketViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.client.force_authenticate(user=self.user)
        self.ticket = Tickets.objects.create(user=self.user, status='unresolved')

    def test_single_ticket_view(self):
        response = self.client.get(reverse('single-ticket', args=[self.ticket.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_ticket_view(self):
        response = self.client.delete(f'/{self.ticket.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TicketMessagesViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.client.force_authenticate(user=self.user)
        self.ticket = Tickets.objects.create(user=self.user, status='unresolved') 

    def test_ticket_messages_view(self):
        data = {
            'message': 'Test message'
        }
        response = self.client.post(reverse('ticket-messages', args=[self.ticket.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Messages.objects.count(), 1)
        self.assertEqual(Messages.objects.first().user, self.user)
