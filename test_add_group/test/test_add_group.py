# -*- coding: utf-8 -*-
from test_add_group.model.group import Group


def test_app_dynamics_job(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group("test name", "group name", "some"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


