from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegistrationSerializer


@api_view(http_method_names=['POST'])
def registration(request):
    serializer = RegistrationSerializer(data=request.POST)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    user = serializer.save()

    # token = Token.objects.get(user=user)
    token = RefreshToken.for_user(user)

    response: dict = dict(refresh=str(token), access=str(token.access_token), **serializer.data)
    return Response(response, status.HTTP_201_CREATED)


@api_view(http_method_names=['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)
