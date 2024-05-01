from django.db.models import QuerySet
from users.models import User

from colors.models import Color, Palette
from colors.repository import ColorRepository
from colors.types import ColorData


class PaletteService:

    def create_palette(self, user: User, name: str) -> Palette:
        palette = Palette.objects.create(name=name, user=user)
        return palette

    def get_base_palette_qs(self, user: User) -> QuerySet[Palette]:
        return Palette.objects.filter(user=user)


class ColorService:
    def __init__(self, color_repository: ColorRepository | None = None):
        self.color_repository = color_repository or ColorRepository()

    def get_palette_colors(self, user: User, palette_id: int) -> QuerySet[Color]:
        return Color.objects.filter(palette_id=palette_id, palette__user=user)

    def get_base_collors_qs(self) -> QuerySet[Palette]:
        return Color.objects.all()

    def create_color(self, data: ColorData):
        name = self.color_repository.get_name_by_hex(data['hex'])
        return Color.objects.create(**data, name=name)
