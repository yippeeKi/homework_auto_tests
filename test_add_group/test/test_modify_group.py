from test_add_group.model.group import Group


def modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    app.group.modify_first_group()
    new_groups = app.group.get_group_list(group)
    group.id = old_groups[0].id
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def modify_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
