import pytest
from contacts.fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login("admin", "secret")

    def fin():
        fixture.session.logout()
        fixture.close()
    request.addfinalizer(fin)
    return fixture
