# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_db(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="Sofia", middlename="Ivanovna", lastname="Petrova", nickname="Sofi",
#                                photo="C:\\Devel\\Andru.jpg", title="prosto test", company="Romashka",
#                                address="Kirova str 5", home="1333434343",
#                                mobile="8923445445", work="2343434444", fax="8923232323", email="sofi@gmail.com",
#                                email2="sofi2@gmail.ru", email3="sofi3@mail.ru", homepage="sofi.net",
#                                bday="19", bmonth="April", byear="1989", aday="6", amonth="May", ayear="1999",
#                                address2="Pervaya str 4",
#                                phone2="1243", note="test contact")
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)