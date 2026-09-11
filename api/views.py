from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView,ListAPIView

from rest_framework import authentication,permissions

from api.serializers import TicketSerializer
from api.models import Ticket

from api.serializers import AdminSerializer
class AdminCreateView(CreateAPIView):
    serializer_class=AdminSerializer


class TicketListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]
    serializer_class=TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)