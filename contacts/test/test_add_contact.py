# -*- coding: utf-8 -*-
from contacts.model.contact_name import ContactName
from contacts.model.contact_company import ContactCompany
from contacts.model.contact_address import ContactAddress
from contacts.model.contact_anniversary import ContactAnniversary
from contacts.model.contact_birthday import ContactBirthday
from contacts.model.contact_contacts import ContactContacts
from contacts.model.contact_extra_contacts import ContactExtraContacts
from contacts.model.contact_mobile import ContactMobile
from contacts.model.contact_work import ContactWork


def test_contacts(app):
    app.session.login("admin", "secret")
    app.contacts.new_contact_name(ContactName("Artem", "AS", "Artemov", "artemka"))
    app.contacts.new_contact_company(ContactCompany("Atom"))
    app.contacts.new_contact_address(ContactAddress("Novosibirsk", "Lenina"))
    app.contacts.new_contact_mobile(ContactMobile("3181818"))
    app.contacts.new_contact_work(ContactWork("Staffcop"))
    app.contacts.new_contact_contacts(ContactContacts("3431212", "artemio.kka", "artemio.kka1@gmail.com",
                                                  "artemio.kka2@gmail.com", "artemio"))
    app.contacts.new_contact_birhday(ContactBirthday("8", "December", "1993"))
    app.contacts.new_contact_anniversary(ContactAnniversary("17", "January", "1998"))
    app.contacts.new_contact_extra_contacts(ContactExtraContacts("Address", "AddressHome", "Test"))
    app.session.logout()
