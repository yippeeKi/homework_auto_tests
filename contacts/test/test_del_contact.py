from contacts.model.contact_name import ContactName

def test_delete_first_contacts(app):
    if app.contacts.count() == 0:
        app.driver.get("http://localhost/addressbook/edit.php")
        app.contacts.new_contact_name(ContactName("Haur", "Nuit", "Geriy", "HGR"))
        app.contacts.new_contact_create()
    app.contacts.delete_first_contact()
