from colors.services import ColorService, PaletteService
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from users.services import UserService

from api.serializers import (
    ColorSerializer,
    ColorSerializerCreate,
    PaletteSerializer,
    UserReadSerializer,
    UserRegistrationSerializer,
)


@extend_schema(tags=['Users'])
class UsersApi(APIView):
    user_service = UserService()
    serializer_class = UserRegistrationSerializer
    serializer_read_class = UserReadSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = self.user_service.create_user(serializer.data)
            response_serializer = self.serializer_read_class(user)
            return Response(response_serializer.data)
        return Response(serializer.errors)


@extend_schema(tags=['Colors'])
class ColorViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAuthenticated]
    color_service = ColorService()
    serializer_class = ColorSerializer

    def get_queryset(self):
        return self.color_service.get_base_collors_qs()

    def create(self, request, *args, **kwargs):
        serializer = ColorSerializerCreate(data=request.data)
        if serializer.is_valid():
            color = self.color_service.create_color(serializer.data)
            serializer = ColorSerializerCreate(color)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@extend_schema(tags=['Palettes'])
class PaletteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PaletteSerializer
    palette_service = PaletteService()
    color_service = ColorService()

    def get_queryset(self):
        return self.palette_service.get_base_palette_qs(self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            palette = self.palette_service.create_palette(request.user, serializer.data['name'])
            serializer = self.serializer_class(palette)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    @extend_schema(tags=['Colors'])
    @action(detail=True, methods=['get'])
    def colors(self, request, pk: int):
        colors = self.color_service.get_palette_colors(request.user, pk)
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)
