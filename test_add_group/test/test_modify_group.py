from test_add_group.model.group import Group


def modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))


def modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))
