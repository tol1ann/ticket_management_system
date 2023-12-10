from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.TicketsListView.as_view(), name="tickets-list"),
    path('<int:pk>/', views.SingleTicketView.as_view(), name="single-ticket"),
    path('create/', views.CreateTicketView.as_view(), name="create-ticket"),
    path('<int:id>/messages/', views.TicketMessagesView.as_view(), name="ticket-messages"),
    path('unresolved/', views.UnresolvedTicketsView.as_view(), name="unresolved-tickets"),
    path('resolved/', views.ResolvedTicketsView.as_view(), name="resolved-tickets"),
    path('freezed/', views.FreezedTicketsView.as_view(), name="freezed-tickets"),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
