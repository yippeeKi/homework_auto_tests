import pytest
from contacts.fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    fixture = Application()
    fixture.session.login("admin", "secret")

    def fin():
        fixture.session.logout()
        fixture.close()
    request.addfinalizer(fin)
    return fixture
