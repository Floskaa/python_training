# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Sofia", middlename="Ivanovna", lastname="Petrova", nickname="Sofi",
                               title="prosto test", company="Romashka", address="Kirova str 5",
                               home="1333434343",
                               mobile="8923445445", work="2343434444", fax="8923232323",
                               email="sofi@gmail.com",
                               email2="sofi2@gmail.ru", email3="sofi3@mail.ru", homepage="sofi.net",
                               address2="Pervaya str 4",
                               phone2="1243", notes="test contact")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)