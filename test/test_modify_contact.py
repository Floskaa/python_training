# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create_for_edit_contact(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(firstname="New update contact"))


