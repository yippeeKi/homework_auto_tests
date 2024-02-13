

def test_delete_first_contacts(app):
    app.session.login("admin", "secret")
    app.contacts.delete_first_contact()
    app.session.logout()