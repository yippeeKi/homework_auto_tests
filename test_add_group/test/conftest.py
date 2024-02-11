from test_add_group.fixture.application import Application

import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.close)
    return fixture
