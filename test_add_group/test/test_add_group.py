# -*- coding: utf-8 -*-
from test_add_group.model.group import Group
from test_add_group.fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.close)
    return fixture


def test_app_dynamics_job(app):
    app.session.login("admin", "secret")
    app.group.create(Group("test name", "group name", "some"))
    app.session.logout()
