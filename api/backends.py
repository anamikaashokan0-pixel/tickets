from django.contrib.auth.backends import BaseBackend
from api.models import User

class PhoneBackend(BaseBackend):

    def authenticate(self, request, username = ..., password = ..., **kwargs):

       try:

           user_object = User.objects.get(phone=username) 

           if user_object.check_password(password):

               return user_object
           else:

               return None
       except:
           return None

    def get_user(self, user_id): 
        
        try:

            return User.objects.get(id=user_id)

        except:

            return None