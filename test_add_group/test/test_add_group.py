# -*- coding: utf-8 -*-
from test_add_group.model.group import Group


def test_app_dynamics_job(app):
    app.group.create(Group("test name", "group name", "some"))

