# -*- coding: utf-8 -*-
from test_add_group.model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group("test name", "group name", "some")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)



