from test_add_group.fixture.application import Application

import pytest


fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login("admin", "secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login("admin", "secret")
    return

@pytest.fixture(autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.close()

    request.addfinalizer(fin)
    return fixture
