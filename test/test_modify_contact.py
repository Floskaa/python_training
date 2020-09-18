# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_for_edit_contact(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New update contact"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

