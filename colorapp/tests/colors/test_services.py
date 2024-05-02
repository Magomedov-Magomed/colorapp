import pytest
from colors.services import ColorService, PaletteService


@pytest.mark.django_db
def test_color_service(user, fake_color_repository):
    color_service = ColorService(fake_color_repository)
    palette_service = PaletteService()
    palette = palette_service.create_palette(user, 'test')
    color = color_service.create_color({"palette_id": palette.id, "hex": "0047AB"})
    assert color.name == 'test_name_0047AB'
