from test_add_group.model.group import Group


def modify_group_name(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group(name="New group"))
    app.session.logout()


def modify_group_header(app):
    app.session.login("admin", "secret")
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()