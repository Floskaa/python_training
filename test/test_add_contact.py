# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            address=random_string("address", 20), home=random_string("home", 20), mobile=random_string("mobile", 20),
            work=random_string("work", 20), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20), address2=random_string("address2", 20),
            phone2=random_string("phone2", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(firstname="Sofia", middlename="Ivanovna", lastname="Petrova", nickname="Sofi",
    #                            photo="C:\\Devel\\Andru.jpg", title="prosto test", company="Romashka",
    #                            address="Kirova str 5", home="1333434343",
    #                            mobile="8923445445", work="2343434444", fax="8923232323", email="sofi@gmail.com",
    #                            email2="sofi2@gmail.ru", email3="sofi3@mail.ru", homepage="sofi.net",
    #                            bday="19", bmonth="April", byear="1989", aday="6", amonth="May", ayear="1999",
    #                            address2="Pervaya str 4",
    #                            phone2="1243", note="test contact")
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