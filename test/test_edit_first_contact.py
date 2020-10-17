# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create_for_edit_contact(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Andrey", middlename="Sergeevich", lastname="Smirnov", nickname="Andru",
                      title="test edit", company="Cheburek", address="Nikolskaya str., 1",
                      home="+7(987)654321",
                      mobile="7(923)445445", work="7(234)3434444", fax="7(923)2323234",
                      email="andru@gmail.com",
                      email2="andru2@gmail.ru", email3="andru3@mail.ru", homepage="andru.net",
                      address2="Vtoraya str 34",
                      phone2="7(904)8888888", notes="test edit contact")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
