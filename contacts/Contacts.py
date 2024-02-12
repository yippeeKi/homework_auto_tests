# -*- coding: utf-8 -*-
from contact_name import ContactName
from contact_company import ContactCompany
from contact_address import ContactAddress
from contact_anniversary import ContactAnniversary
from contact_birthday import ContactBirthday
from contact_contacts import ContactContacts
from contact_extra_contacts import ContactExtraContacts
from contact_mobile import ContactMobile
from contact_work import ContactWork
import pytest
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.close)
    return fixture


def test_contacts(app):
    app.login("admin", "secret")
    app.new_contact_name(ContactName("Artem", "AS", "Artemov", "artemka"))
    app.new_contact_company(ContactCompany("Atom"))
    app.new_contact_address(ContactAddress("Novosibirsk", "Lenina"))
    app.new_contact_mobile(ContactMobile("3181818"))
    app.new_contact_work(ContactWork("Staffcop"))
    app.new_contact_contacts(ContactContacts("3431212", "artemio.kka", "artemio.kka1@gmail.com",
                                                  "artemio.kka2@gmail.com", "artemio"))
    app.new_contact_birhday(ContactBirthday("8", "December", "1993"))
    app.new_contact_anniversary(ContactAnniversary("17", "January", "1998"))
    app.new_contact_extra_contacts(ContactExtraContacts("Address", "AddressHome", "Test"))
    app.logout()
