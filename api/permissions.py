from rest_framework.permissions import BasePermission

from api.models import Ticket

class Userownly (BasePermission):

    def has_object_permission(self, request, view, obj):

        if isinstance(obj,Ticket):

            return request.user==obj.created_by
        
