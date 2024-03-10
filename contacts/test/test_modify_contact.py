from contacts.model.contact_name import ContactName


def test_modify_contacts_name(app):
    if app.contacts.count() == 0:
        app.driver.get("http://localhost/addressbook/edit.php")
        app.contacts.new_contact_name(ContactName("Haur", "Nuit", "Geriy", "HGR"))
        app.contacts.new_contact_create()

    app.contacts.modify_first_contact(ContactName("Buka", "Haripovich",
                                                  "Garinov", "Hp"))

