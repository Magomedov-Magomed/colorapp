import logging

import requests

logger = logging.getLogger(__name__)


class ColorRepository:
    base_url = 'https://www.thecolorapi.com/'

    def get_name_by_hex(self, hex: str) -> str:
        try:
            resp = requests.get(self.base_url + f"id?hex={hex}", timeout=5)
            resp.raise_for_status()
            resp = resp.json()
            return resp['name']['value']
        except requests.RequestException:
            logger.exception('Get color name failed')
