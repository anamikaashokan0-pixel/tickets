from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView

from rest_framework import authentication,permissions

from api.serializers import TicketSerializer,SignUpSerializer,TicketCommentSerializer
from api.models import Ticket,TicketComment
from api.permissions import Userownly

from api.serializers import AdminSerializer


from api.agent import evaluate_response

class AdminCreateView(CreateAPIView):
    serializer_class=AdminSerializer

class StaffCreateView(CreateAPIView):
    serializer_class=SignUpSerializer


class TicketListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]
    serializer_class=TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)


class TicketUpdateDeleteView(UpdateAPIView,DestroyAPIView):
    
    serializer_class=TicketSerializer
    queryset = Ticket.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[Userownly]


class TicketRetrieveView(RetrieveAPIView):
    queryset=Ticket.objects.all()
    serializer_class=TicketSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

class TicketCommentView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    
    def get(self,request,pk):

        ticket=Ticket.objects.get(id=pk)
        ticketcomment=TicketComment.objects.filter(ticket=ticket)
        serializer=TicketCommentSerializer(ticketcomment,many=True)

        return Response(serializer.data)

    def post(self,request,pk):
    
        ticket=Ticket.objects.get(id=pk)
        message=request.data.get("message")

        result=evaluate_response(ticket)

        print(result)
        TicketComment.objects.create(
            ticket=ticket,
            user=request.user,
            message=message
        )

    
        return Response({"message":"commented...."})
    


