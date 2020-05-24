import os
import tempfile

import pytest

from models import Campsite

campsite = Campsite(
        image_url = 'www.example.com',
        city = 'Fruita',
        state = 'CO',
        name = '18 Road',
        description = 'Awesome',
        driving_tips = 'Turn Left, then right',
        lon = 18.4,
        lat = 17.2,
        datetime = 124
        )

def test_attributes():
    assert campsite.name == '18 Road'
    assert campsite.image_url == 'www.example.com'
    assert campsite.city == 'Fruita'
    assert campsite.state == 'CO'
    assert campsite.description == 'Awesome'
    assert campsite.driving_tips == 'Turn Left, then right'
    assert campsite.lon == 18.4
    assert campsite.lat == 17.2
    assert campsite.datetime == 124
