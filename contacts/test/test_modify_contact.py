from contacts.model.contact_name import ContactName


def test_modify_contacts_name(app):
    app.contacts.modify_first_contact(ContactName("Zuka", "Haripovich", "Garinov", "Hp"))