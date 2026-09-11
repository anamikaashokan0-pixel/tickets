from rest_framework import serializers

from api.models import User,Ticket,TicketComment

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","phone","password"]
        read_only_fields=["id"]

    def create(self,validated_data):
        return User.objects.create_superuser(**validated_data)

    
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","phone","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields="__all__"
        read_only_fields=["id","created_by","assigned_to","created_at","updated_at"]

class TicketCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=TicketComment
        fields="__all__"
        read_only_fields=["id","created_at"]