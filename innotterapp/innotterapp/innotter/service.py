import jwt, datetime
from django.contrib import auth
from rest_framework import status
from rest_framework.response import Response

from django.conf import settings
from innotter.serializers import UserSerializer


def login_user(request):
    data = request.data
    username = data.get('username', '')
    password = data.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user:
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=50000),
            'iat': datetime.datetime.utcnow()
        }
        auth_token = jwt.encode(
            payload, settings.JWT_SECRET_KEY, algorithm="HS256")

        serializer = UserSerializer(user)

        data = {'user': serializer.data, 'token': auth_token}

        return data
        
    return False


def get_new_follower_id(self, request):
    id = request.user.id

    page = self.get_object()

    if page.is_private:
        page.follow_requests.add(id)
    
    else:
        page.followers.add(id)   

    return id
