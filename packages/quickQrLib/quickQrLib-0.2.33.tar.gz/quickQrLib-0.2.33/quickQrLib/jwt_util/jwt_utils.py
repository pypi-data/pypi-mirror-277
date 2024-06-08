import requests
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.state import token_backend
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class CustomJWTAuthentication(JWTAuthentication):
    def __init__(self, *args, **kwargs):
        self.url = kwargs.pop('url', None)
        super().__init__(*args, **kwargs)

    def authenticate(self, request, url):
        header = self.get_header(request)
        if header is None:
            raise AuthenticationFailed("Authorization credentials were not provided")

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise AuthenticationFailed("Authorization credentials were not provided")
        
        try:
            validated_token = token_backend.decode(raw_token, verify=True)
        except Exception as e:
            raise InvalidToken(e) from e
       
        response = requests.post(url, data={'token': raw_token})
        if response.status_code == 200:
            # return self.get_user(response.json()), raw_token
            return super().authenticate(request)
        else:
            raise AuthenticationFailed("Invalid token")        
