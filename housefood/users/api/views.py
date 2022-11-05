from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

from users.models import User
from users.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    # permiso para ver quien usara los endpoint
    permission_classes = [IsAdminUser]
    # esto es para ver como queremos que nos devuelva los datos
    serializer_class = UserSerializer
    queryset = User.objects.all()  # es para ver a que modelo queremos llegar

    def create(self, request, *args, **kwargs):
        # esto es para encriptar la contraseña
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
