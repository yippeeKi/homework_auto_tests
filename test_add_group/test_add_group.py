# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.close)
    return fixture


def test_app_dynamics_job(app):
    app.login("admin", "secret")
    app.create_group(Group("test name", "group name", "some"))
    app.logout()
